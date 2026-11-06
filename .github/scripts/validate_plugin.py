#!/usr/bin/env python3
"""Validate the plugin repo. Stdlib only. Usage: validate_plugin.py [--base <git-ref>]"""
import argparse
import json
import re
import struct
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO_URL = "https://github.com/tejitpabari99/tejit-np-plugin"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
errors = []


def err(msg):
    errors.append(msg)


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        err(f"{path.relative_to(ROOT)}: invalid or unreadable JSON: {e}")
        return None


def semver_tuple(v):
    m = SEMVER.match(v or "")
    return tuple(int(x) for x in m.groups()[:3]) if m else None


def frontmatter(text):
    """Return (name, description, metadata_version) from simple YAML frontmatter."""
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return None
    block = m.group(1)
    name = re.search(r"^name:\s*(.+?)\s*$", block, re.M)
    desc = re.search(r"^description:\s*(.+?)\s*$", block, re.M)
    meta = re.search(r"^metadata:\s*\n((?:[ \t]+.*\n?)+)", block + "\n", re.M)
    ver = None
    if meta:
        v = re.search(r"^[ \t]+version:\s*['\"]?([^'\"\s]+)['\"]?\s*$", meta.group(1), re.M)
        ver = v.group(1) if v else None
    return (name.group(1).strip("'\"") if name else None,
            desc.group(1) if desc else None, ver)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def check_json_and_names():
    mp_path = ROOT / ".claude-plugin" / "marketplace.json"
    pj_path = ROOT / ".claude-plugin" / "plugin.json"
    mp, pj = load_json(mp_path), load_json(pj_path)
    if not (mp and pj):
        return None
    if "version" in mp:
        err("marketplace.json must not have a top-level 'version'")
    for i, p in enumerate(mp.get("plugins", [])):
        if "version" in p:
            err(f"marketplace.json plugins[{i}] must not have 'version'")
    names = [p.get("name") for p in mp.get("plugins", [])]
    if pj.get("name") not in names:
        err(f"marketplace plugin entry name {names} != plugin.json name {pj.get('name')!r}")
    for key in ("repository", "homepage"):
        if pj.get(key) != REPO_URL:
            err(f"plugin.json {key} is {pj.get(key)!r}, expected {REPO_URL!r}")
    ver = pj.get("version")
    if not semver_tuple(ver):
        err(f"plugin.json version {ver!r} is not valid semver")
    else:
        cl = (ROOT / "CHANGELOG.md")
        if not cl.exists() or not re.search(r"^## " + re.escape(ver) + r" \(", cl.read_text(encoding="utf-8"), re.M):
            err(f"CHANGELOG.md has no '## {ver} (' section")
    return pj


def skill_dirs():
    return sorted(p.parent for p in (ROOT / "skills").glob("*/SKILL.md"))


def check_skills():
    for d in skill_dirs():
        fm = frontmatter((d / "SKILL.md").read_text(encoding="utf-8"))
        rel = f"skills/{d.name}/SKILL.md"
        if not fm:
            err(f"{rel}: missing frontmatter")
            continue
        name, desc, ver = fm
        if not name:
            err(f"{rel}: frontmatter missing name")
        elif name != d.name:
            err(f"{rel}: name {name!r} does not match folder {d.name!r}")
        if not desc:
            err(f"{rel}: frontmatter missing description")
        if not ver:
            err(f"{rel}: frontmatter missing metadata.version")
        elif not semver_tuple(ver):
            err(f"{rel}: metadata.version {ver!r} is not valid semver")


def check_references():
    pat = re.compile(r"`((?:prompts/|templates/|references/|scripts/|\.\./)[^`\s]*)`")
    for f in sorted((ROOT / "skills").rglob("*.md")):
        parts = f.relative_to(ROOT / "skills").parts
        skill_root = ROOT / "skills" / parts[0]
        for m in pat.finditer(f.read_text(encoding="utf-8")):
            ref = m.group(1)
            if any(c in ref for c in "<>*{}"):
                continue
            if not ((skill_root / ref).exists() or (f.parent / ref).exists()):
                err(f"{f.relative_to(ROOT)}: broken reference `{ref}`")


def check_old_names():
    # Patterns are assembled so this file never matches itself.
    old = ["tejit-non-" + "profit", "tejit-non-" + "profit-mkt",
           "plugins" + "/"]
    files = git("ls-files").stdout.splitlines()
    for rel in files:
        if rel.startswith(".github/"):
            continue
        p = ROOT / rel
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        for o in old:
            if o in text:
                err(f"{rel}: contains old name or path {o!r}")


def check_release_files(pj):
    """License, Gemini manifest, icon."""
    if pj.get("license") != "MIT":
        err(f"plugin.json license is {pj.get('license')!r}, expected 'MIT'")
    if not (ROOT / "LICENSE").is_file():
        err("LICENSE file is missing")
    gp = ROOT / "gemini-extension.json"
    if not gp.is_file():
        err("gemini-extension.json is missing")
    else:
        g = load_json(gp)
        if g is not None:
            for key in ("name", "version", "description"):
                if g.get(key) != pj.get(key):
                    err(f"gemini-extension.json {key} {g.get(key)!r} != plugin.json {pj.get(key)!r}")
    ip = ROOT / ".claude-plugin" / "icon.png"
    if not ip.is_file():
        err(".claude-plugin/icon.png is missing")
        return
    head = ip.read_bytes()[:24]
    if head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        err(".claude-plugin/icon.png is not a PNG")
        return
    w, h = struct.unpack(">II", head[16:24])
    if w != h or not 512 <= w <= 2048:
        err(f".claude-plugin/icon.png is {w}x{h}, must be square and 512 to 2048 px")


def check_skill_docs():
    for d in skill_dirs():
        f = ROOT / "docs" / "skills" / f"{d.name}.md"
        if not f.is_file():
            err(f"docs/skills/{d.name}.md is missing")
        elif "```mermaid" not in f.read_text(encoding="utf-8"):
            err(f"docs/skills/{d.name}.md has no ```mermaid block")


def check_neutral_wording():
    allowed = {ROOT / "skills/partner-event-finder/prompts/00-update-check.md"}
    targets = [ROOT / "CONNECTORS.md"]
    for sub in ("skills", "guides"):
        targets += [p for p in (ROOT / sub).rglob("*") if p.is_file()]
    for f in sorted(targets):
        if f in allowed:
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            continue
        text = text.replace(".claude-plugin", "")
        if re.search(r"\bClaude\b", text):
            err(f"{f.relative_to(ROOT)}: uses the word 'Claude'; use 'your AI assistant' instead")


def check_feedback_form():
    f = ROOT / ".github" / "ISSUE_TEMPLATE" / "feedback.yml"
    if not f.is_file():
        err(".github/ISSUE_TEMPLATE/feedback.yml is missing")
        return
    text = f.read_text(encoding="utf-8")
    for fid in ("type", "tool_goal", "details", "importance", "example", "contact", "version"):
        if not re.search(r"^\s*id:\s*" + fid + r"\s*$", text, re.M):
            err(f"feedback.yml is missing field id {fid!r}")
    if not re.search(r"^labels:.*\bfeedback\b", text, re.M):
        err("feedback.yml does not apply the 'feedback' label")


def check_feedback_email():
    f = ROOT / "skills" / "share-feedback" / "SKILL.md"
    if not f.is_file() or "tejitpabari99@gmail.com" not in f.read_text(encoding="utf-8"):
        err("skills/share-feedback/SKILL.md must contain tejitpabari99@gmail.com (email route)")


def check_links():
    link = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)\)|!\[[^\]]*\]\(([^)\s]+)\)|src=\"([^\"]+)\"")
    files = [ROOT / "README.md"] + sorted((ROOT / "docs").rglob("*.md"))
    for f in files:
        text = re.sub(r"```.*?```", "", f.read_text(encoding="utf-8"), flags=re.S)
        for m in link.finditer(text):
            target = next(g for g in m.groups() if g)
            if re.match(r"^(https?:|mailto:|#)", target):
                continue
            path = target.split("#")[0]
            if path and not (f.parent / path).exists():
                err(f"{f.relative_to(ROOT)}: broken link {target}")


def check_base(base, pj):
    if git("rev-parse", "--verify", base).returncode != 0:
        err(f"--base ref {base!r} not found")
        return
    show = git("show", f"{base}:.claude-plugin/plugin.json")
    if show.returncode != 0:
        print(f"base {base} has no .claude-plugin/plugin.json: skipping version-bump checks")
        return
    watched = ["skills/", ".claude-plugin/plugin.json", "CONNECTORS.md", "guides/"]
    diff = git("diff", "--name-only", f"{base}...HEAD", "--", *watched)
    changed = [l for l in diff.stdout.splitlines() if l]
    if not changed:
        print("no plugin files changed versus base: skipping version-bump checks")
        return
    try:
        base_ver = json.loads(show.stdout).get("version")
    except Exception as e:  # noqa: BLE001
        err(f"base plugin.json invalid JSON: {e}")
        return
    new, old = semver_tuple(pj.get("version")), semver_tuple(base_ver)
    if new and old and not new > old:
        err(f"plugin version {pj.get('version')} must be higher than base {base_ver} (changed: {', '.join(changed[:5])})")
    for name in sorted({c.split("/")[1] for c in changed if c.startswith("skills/") and c.count("/") >= 2}):
        cur_p = ROOT / "skills" / name / "SKILL.md"
        cur = frontmatter(cur_p.read_text(encoding="utf-8"))[2] if cur_p.exists() else None
        b = git("show", f"{base}:skills/{name}/SKILL.md")
        if b.returncode != 0:
            continue  # new skill
        bfm = frontmatter(b.stdout)
        bver = bfm[2] if bfm else None
        if not cur:
            continue  # reported by check_skills
        if semver_tuple(cur) and semver_tuple(bver) and not semver_tuple(cur) > semver_tuple(bver):
            err(f"skills/{name} changed but metadata.version {cur} is not higher than base {bver}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base")
    a = ap.parse_args()
    pj = check_json_and_names()
    check_skills()
    check_references()
    check_old_names()
    if pj:
        check_release_files(pj)
    check_skill_docs()
    check_neutral_wording()
    check_feedback_form()
    check_feedback_email()
    check_links()
    if a.base and pj:
        check_base(a.base, pj)
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("OK: all checks passed")


if __name__ == "__main__":
    main()
