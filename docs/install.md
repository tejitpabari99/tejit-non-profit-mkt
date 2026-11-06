# Install

Pick the tool you use. In every case the assistant needs access to **Google Drive, Google Sheets, Google Calendar and the web** (the skill helps you switch these on the first time).

After installing, start a new chat and say **"Tejit's non profit tools"**.

## What was tested
- Tested: Claude Code and GitHub Copilot CLI installs.
- Gemini CLI: see the note in its section.
- Not tested by us: Claude website or desktop, ChatGPT, Codex, VS Code. These steps come from each vendor's documentation and may change.

## Claude website or desktop app
1. Open **Customize**, then **Plugins**.
2. Choose **Add**, then **Add marketplace**.
3. Paste `tejitpabari99/tejit-np-plugin` and confirm.
4. Choose **Install**.
5. Turn on **Sync automatically** so you always get the newest version.

## Claude Code
Version 2.1.275 or later:
```
/plugin install tejit-np-plugin --marketplace tejitpabari99/tejit-np-plugin
```
Older versions:
```
/plugin marketplace add tejitpabari99/tejit-np-plugin
/plugin install tejit-np-plugin@tejit-np-plugin
```
Then turn on updates once: type `/plugin`, open **Marketplaces**, select `tejit-np-plugin`, choose **Enable auto-update**.

## ChatGPT Business or Enterprise
A workspace admin opens **Admin**, then **Plugins**, and imports the GitHub repository `tejitpabari99/tejit-np-plugin`. It syncs daily. It is not in the public directory yet.

## Codex
```
codex plugin marketplace add tejitpabari99/tejit-np-plugin
```

## GitHub Copilot CLI
```
copilot plugin marketplace add tejitpabari99/tejit-np-plugin
copilot plugin install tejit-np-plugin@tejit-np-plugin
```
Update later with `copilot plugin update tejit-np-plugin`.

In VS Code, use **Add Marketplace** in Agent Customizations.

## Gemini CLI
```
gemini extensions install https://github.com/tejitpabari99/tejit-np-plugin --auto-update
```
Update later with `gemini extensions update tejit-np-plugin`.

Note: Google has replaced Gemini CLI with Antigravity CLI for unpaid and Google One users. Gemini CLI still applies to the accounts Google keeps it for.

GEMINI_TEST_NOTE

## Other tools
Build a ZIP (see [releasing.md](releasing.md)) and upload it in the tool's plugin or skill upload screen.

## Updating
- With auto-update or sync on, new versions arrive on their own.
- Each time you use the tool, it also checks for a newer version and tells you how to update.
