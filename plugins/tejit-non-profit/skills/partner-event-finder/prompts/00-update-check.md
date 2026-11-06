# Step 0: update check (runs before every task, in every skill)

Goal: make sure the person works with the newest version and that their saved project has the newest improvements, before anything else. Be brief and calm. Say nothing if nothing changed except one friendly line.

Never show the person version numbers, file names, or technical detail. High level only.

## 1. Gather (silently)
- **Installed version:** this skill's frontmatter `metadata.version` (same as the plugin's `plugin.json` version).
- **Project version:** `plugin_version` in the project's `metadata.txt` (if a project exists). Missing = created by a test build before 0.1.0.
- **Source:** `plugin_source` in the root `metadata.txt` (Drive folder `tejit-non-profit-claude`), else the plugin's `repository` field. If it is a GitHub address, the newest files are readable at `https://raw.githubusercontent.com/<owner>/<repo>/main/`.

## 2. Is there a newer plugin version?
Try to read the newest `plugins/tejit-non-profit/.claude-plugin/plugin.json` from the source (marketplace layout) and compare its `version` with the installed one. If it cannot be read, skip quietly.
- **Newer exists:** tell the person once, in plain words: "A newer version of this tool is available." Then explain how to get it:
  - In Claude Code: type `/plugin`, open **Marketplaces**, pick `tejit-non-profit`, choose **Update marketplace** (or turn on **Enable auto-update** so it never needs doing again).
  - In the Claude app: open the plugin's page in your plugins list and update it there.
  Ask whether they want to update now and come back, or continue with the current version. Do not block them: if they continue, carry on with the installed version. A plugin cannot replace its own files, so never claim you updated it.
- **Same version:** say nothing.

## 3. Apply the changes to the project (the part you CAN do)
If a project exists and its `plugin_version` is older than the installed version:
1. Say: "Checking for improvements to your project… I found some. Applying them now." (high level only)
2. Read the plugin's `CHANGELOG.md` (in the plugin folder; if unavailable read it from the source). Collect every version section newer than the project version, oldest first.
3. In each section, read **Project changes** only. Perform the items that relate to Partner Event Finder (for example adding a column to the project sheet, filling a new field), in order, before the task. Only change files this plugin created. Never delete data; if something is unclear or risky, ask first.
4. Write the new `plugin_version` (and `plugin_source`) into the project `metadata.txt` and the root `metadata.txt` (create-new then trash-old rule).
5. Tell the person: "All up to date. Here's what's new for you:" with one short bullet per change in everyday words.

If nothing needed doing, continue silently.
