#!/usr/bin/env python3
"""Merge duplicate organizations. Optional helper; if code can't run, do the same by reasoning.

Input : JSON list of {"key": "...", "name": "...", "website": "..."} on stdin.
Arg   : --strength strong|weak
Output: JSON list of {"org_id": "ORG-001", "source_keys": ["k1","k2"], "name": ..., "website": ...}

strong: rows with the same key merge exactly.
weak  : rows merge when the normalized website matches, or the normalized name matches.
Near-misses (weak) are listed under "maybe" on stderr for the guide to confirm with the person.
"""
import sys, json, re, argparse
from difflib import SequenceMatcher

def norm_name(s):
    s = re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())
    s = re.sub(r"\b(the|inc|incorporated|llc|ltd|foundation|org)\b", " ", s)
    return " ".join(s.split())

def norm_site(s):
    s = (s or "").lower().strip()
    s = re.sub(r"^https?://", "", s); s = re.sub(r"^www\.", "", s)
    return s.rstrip("/")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--strength", required=True, choices=["strong", "weak"])
    a = ap.parse_args(); rows = json.load(sys.stdin)
    groups, maybe = [], []
    for r in rows:
        placed = False
        for g in groups:
            if a.strength == "strong":
                hit = r["key"] and r["key"] in g["source_keys"]
            else:
                hit = (norm_site(r.get("website")) and norm_site(r.get("website")) == norm_site(g.get("website"))) \
                      or (norm_name(r["name"]) and norm_name(r["name"]) == norm_name(g["name"]))
                if not hit and SequenceMatcher(None, norm_name(r["name"]), norm_name(g["name"])).ratio() > 0.88:
                    maybe.append([r["name"], g["name"]])
            if hit:
                if r["key"] not in g["source_keys"]: g["source_keys"].append(r["key"])
                placed = True; break
        if not placed:
            groups.append({"source_keys": [r["key"]], "name": r["name"], "website": r.get("website", "")})
    for i, g in enumerate(groups, 1): g["org_id"] = f"ORG-{i:03d}"
    if maybe: print("maybe duplicates:", json.dumps(maybe), file=sys.stderr)
    json.dump(groups, sys.stdout, indent=1)

if __name__ == "__main__": main()
