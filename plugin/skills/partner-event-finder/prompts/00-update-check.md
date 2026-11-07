# Step 0: update check (runs before every task, in every skill)

Goal: make sure the person works with the newest version and that their saved project has the newest improvements, before anything else. Be brief and calm. Say nothing if nothing changed except one friendly line.

Never show the person version numbers, file names, or technical detail. High level only.

## 1. Gather (silently)
- **Installed version:** this skill's frontmatter `metadata.version` (same as the plugin's `plugin.json` version).
- **Project version:** `plugin_version` in the project's `metadata.txt` (if a project exists). Missing = created by a test build before 0.1.0.
- **Source:** `plugin_source` in the root `metadata.txt` (Drive folder `tejit-np-plugin`), else the plugin's `repository` field. If it is a GitHub address, the newest files are readable at `https://raw.githubusercontent.com/<owner>/<repo>/main/`.

## 2. Is there a newer plugin version?
Try to read the newest `plugin/.claude-plugin/plugin.json` of the source (on GitHub: `plugin/.claude-plugin/plugin.json` under the raw address above) and compare its `version` with the installed one. If it cannot be read, skip quietly.
- **Newer exists:** tell the person once, in plain words: "A newer version of this tool is available." Then explain how to get it:
  Tell them to use their tool's plugin update option. Short examples:
  - Claude Code: type `/plugin`, open **Marketplaces**, pick `tejit-np-plugin` (the marketplace has the same name as the plugin), choose **Update marketplace** (or turn on **Enable auto-update** so it never needs doing again).
  - Claude app: open the plugin's page in your plugins list and update it there.
  - GitHub Copilot: run `copilot plugin update tejit-np-plugin`.
  - Gemini CLI: run `gemini extensions update tejit-np-plugin`.
  - Installed from a ZIP file: download the newest ZIP from the plugin's GitHub page and upload it again.
  If their tool is not listed, tell them to look for an update option on the plugin's page.
  Ask whether they want to update now and come back, or continue with the current version. Do not block them: if they continue, carry on with the installed version. A plugin cannot replace its own files, so never claim you updated it.
- **Same version:** say nothing.

## 3. Apply the changes to the project (the part you CAN do)
If a project exists and its `plugin_version` is older than the installed version:
1. Say: "Checking for improvements to your project… I found some. Applying them now." (high level only)
2. Read the plugin's `CHANGELOG.md` (at the plugin root; if unavailable read `plugin/CHANGELOG.md` from the source). Collect every version section newer than the project version, oldest first.
3. In each section, read **Project changes** only. Perform the items that relate to Partner Event Finder (for example adding a column to the project sheet, filling a new field), in order, before the task. Only change files this plugin created. Never delete data; if something is unclear or risky, ask first.
4. Write the new `plugin_version` (and `plugin_source`) into the project `metadata.txt` and the root `metadata.txt` (create-new then trash-old rule).
5. Tell the person: "All up to date. Here's what's new for you:" with one short bullet per change in everyday words.

If nothing needed doing, continue silently.
