# Releasing

## Steps
1. Change the plugin and add a section to `plugin/CHANGELOG.md`.
2. Bump `version` in `plugin/.claude-plugin/plugin.json`, in `plugin/gemini-extension.json` (must match), and `metadata.version` in any changed skill. Without a new version number, people will not receive the change.
3. Run `claude plugin validate .`, `claude plugin validate plugin` and `python3 .github/scripts/validate_plugin.py`.
4. Open a pull request into `main` and merge it.

## What CI checks
On every pull request (`.github/workflows/validate.yml`):
- The plugin validates, and JSON and skill frontmatter are well formed.
- The changelog has a section for the plugin version.
- Referenced files exist and relative links in `README.md` and `docs/` resolve.
- `plugin/gemini-extension.json` matches `plugin.json` (name, version, description).
- The license is MIT, `LICENSE` exists, and `plugin/.claude-plugin/icon.png` is a square PNG between 512 and 2048 pixels.
- The feedback form `.github/ISSUE_TEMPLATE/feedback.yml` exists with its field ids and the `feedback` label.
- Each skill has a page in `docs/skills/` with a Mermaid flow.
- The plain word "Claude" is not used in `plugin/skills/`, `plugin/CONNECTORS.md` or `plugin/guides/` (except the update-check prompt).
- When plugin files changed, the plugin version and each changed skill's version are higher than on `main`.
- `TERMS.md` and `PRIVACY.md` exist, link to each other, and are linked from `README.md`; the usage-ping recipes (`identity.md`, `usage-ping.md`) exist with the exact notice text, the uid snippet, and no `reason`; `start`, `partner-event-finder` and `install-automation` reference them, and `share-feedback` does not.
- The ZIP builds, and holds the plugin files but no `.github/` or `docs/`.

## Building a ZIP
For tools that take an upload instead of a marketplace. Python 3 only, any OS:
```
python3 scripts/build_zip.py
```
This writes `dist/tejit-np-plugin-<version>.zip` (version read from `plugin.json`). It holds the contents of `plugin/` (`.claude-plugin/`, `gemini-extension.json`, `skills/`, `guides/`, `CHANGELOG.md`, `CONNECTORS.md`) plus `LICENSE` and `README.md` at the ZIP root.

For portals that take one skill at a time:
```
python3 scripts/build_zip.py --skill partner-event-finder
```
This writes `dist/partner-event-finder-<version>.zip` with `SKILL.md` at the ZIP root. It warns if the skill points to files outside its own folder (`../`), because those would be missing.

`dist/` is not committed.
