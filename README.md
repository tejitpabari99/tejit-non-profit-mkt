# Tejit's Non Profit Tools

Small, guided Claude helpers for nonprofits, created by Tejit Pabari.

## Skills
- **`start`**: friendly front door. Explains plugins and skills, shows where the plugin came from, lists the skills, and hands off to the one you pick.
- **`partner-event-finder`**: finds where partner organizations announce fundraising events, saves the links (plus a short description and website per organization) in a Google Sheet, and, after you say yes, adds the events to a separate Google Calendar. Works in rounds of at most 20 organizations.

Each skill carries its own version in its `SKILL.md` frontmatter (`metadata.version`).

## Install in Claude (website or desktop app)
1. Go to [claude.ai](https://claude.ai) or open the Claude desktop app, and sign in.
2. Open **Customize**, then **Plugins**.
3. Choose **Add**, then **Add marketplace**.
4. Paste `tejitpabari99/tejit-np-plugin` and confirm.
5. Find **Tejit's Non Profit Tools** and choose **Install**.
6. On the marketplace, turn on **Sync automatically** so you always get the newest version.
7. Start a new chat and say **"Tejit's non profit tools"**.

## Install in Claude Code
```
/plugin install tejit-np-plugin --marketplace tejitpabari99/tejit-np-plugin
```
This needs Claude Code 2.1.275 or later. On older versions:
```
/plugin marketplace add tejitpabari99/tejit-np-plugin
/plugin install tejit-np-plugin@tejit-np-plugin
```
Then turn on updates once: type `/plugin`, open **Marketplaces**, select `tejit-np-plugin`, and choose **Enable auto-update**.

## Updates
- With **Sync automatically** or **Enable auto-update** on, new versions arrive on their own.
- Each time you use the tool, it also checks for a newer version. If there is one, it tells you how to update and lets you choose to update now or carry on.

## For the maintainer: releasing a new version
1. Change the plugin and add a section to `CHANGELOG.md`.
2. Bump `version` in `.claude-plugin/plugin.json`, and `metadata.version` in any changed skill. Without a new version number, people will not receive the change.
3. Run `claude plugin validate .`
4. Open a pull request into `main` and merge it.

CI (`.github/workflows/validate.yml`) enforces these on every pull request: the plugin validates, JSON and frontmatter are well formed, the changelog has a section for the plugin version, referenced files exist, and, when plugin files changed, the plugin version and each changed skill's `metadata.version` are higher than on `main`.

See `CHANGELOG.md` for versions.

## What is inside

```
tejit-np-plugin/                   (repo root = the plugin)
├── .claude-plugin/
│   ├── plugin.json                plugin name, version
│   └── marketplace.json           marketplace listing (source: ./)
├── .github/
│   ├── scripts/validate_plugin.py checks used by CI
│   └── workflows/validate.yml     runs the checks on pull requests and pushes to main
├── README.md                      (this file)
├── CHANGELOG.md                   versions, update guidelines, project changes
├── CONNECTORS.md                  connections used
├── guides/
│   └── sharing-the-calendar.md
└── skills/
    ├── start/                     welcome, skills list, source record
    └── partner-event-finder/
        ├── SKILL.md               short router: decides which prompt to follow
        ├── prompts/               the flow, one file per phase (loaded only when needed)
        │   ├── 00-update-check.md   runs first, every time
        │   ├── 01-intro-and-permissions.md
        │   ├── 02-onboarding-setup.md
        │   ├── 03-find-sources.md
        │   ├── 04-collect-events.md
        │   └── 05-run-log.md      runs at the end of every run
        ├── templates/             exact chat wording, followed directly for a consistent experience
        │   ├── skill-about.md
        │   ├── permission-help.md
        │   ├── access-confirmation.md
        │   ├── step-explainers.md
        │   ├── calendar-instructions.md
        │   ├── run-flow.md
        │   ├── folder-and-sheet-links.md
        │   └── closing.md
        ├── scripts/
        │   └── dedupe_orgs.py     merges duplicate organizations using the foreign key
        └── references/            schemas (sheet, metadata, calendar event format)
```

## Where things are saved in Google Drive
```
tejit-np-plugin/
├── metadata.txt                     (where the plugin came from; version)
└── partner-event-finder/
    └── <project name>/
        ├── <project name> sources   (Google Sheet: Organizations, Sources, Log)
        └── metadata.txt             (settings; you never need to edit it)
```

## Safety
- Your original sheet and documents are only ever read, never edited.
- Events go only into the separate calendar you pick. Nothing is ever deleted.
- A page the tool cannot read is reported, never counted as "no events".

## Honest limits
It can only find what partners publish. Facebook and Instagram are not read in this version. It cannot create a calendar for you; the skill shows you how (one minute).
