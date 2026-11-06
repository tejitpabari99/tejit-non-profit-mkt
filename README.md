# Tejit's Non Profit Tools

Small, guided Claude helpers for nonprofits, created by Tejit Pabari.

## Skills
- **Partner Event Finder**: finds where partner organizations announce fundraising events and adds them to a shared Google Calendar.

## Install in Claude (website or desktop app)
1. Go to [claude.ai](https://claude.ai) or open the Claude desktop app, and sign in.
2. Open **Customize**, then **Plugins**.
3. Choose **Add**, then **Add marketplace**.
4. Paste `tejitpabari99/tejit-non-profit-mkt` and confirm.
5. Find **Tejit's Non Profit Tools** and choose **Install**.
6. On the marketplace, turn on **Sync automatically** so you always get the newest version.
7. Start a new chat and say **"Tejit's non profit tools"**.

## Install in Claude Code
```
/plugin install tejit-non-profit --marketplace tejitpabari99/tejit-non-profit-mkt
```
This needs Claude Code 2.1.275 or later. On older versions:
```
/plugin marketplace add tejitpabari99/tejit-non-profit-mkt
/plugin install tejit-non-profit@tejit-non-profit-marketplace
```
Then turn on updates once: type `/plugin`, open **Marketplaces**, select `tejit-non-profit-marketplace`, and choose **Enable auto-update**.

## Updates
- With **Sync automatically** or **Enable auto-update** on, new versions arrive on their own.
- Each time you use the tool, it also checks for a newer version. If there is one, it tells you how to update and lets you choose to update now or carry on.

## For the maintainer: releasing a new version
1. Change the plugin and add a section to `plugins/tejit-non-profit/CHANGELOG.md`.
2. Bump `version` in `plugins/tejit-non-profit/.claude-plugin/plugin.json`, and `metadata.version` in any changed skill. Without a new version number, people will not receive the change.
3. Run `claude plugin validate .`
4. Open a pull request into `main` and merge it.

See `plugins/tejit-non-profit/CHANGELOG.md` for versions.
