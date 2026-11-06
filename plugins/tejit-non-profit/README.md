# tejit-non-profit

**Tejit's Non Profit Tools**: a Claude plugin of small, guided helpers for nonprofits, created by Tejit Pabari. Version 0.1.0. See `CHANGELOG.md` for versions and update guidelines.

## Skills
- **`start`**: friendly front door. Explains plugins and skills, shows where the plugin came from, lists the skills, and hands off to the one you pick.
- **`partner-event-finder`**: finds where partner organizations announce fundraising events, saves the links (plus a short description and website per organization) in a Google Sheet, and, after you say yes, adds the events to a separate Google Calendar. Works in rounds of at most 20 organizations.

Each skill carries its own version in its `SKILL.md` frontmatter (`metadata.version`).

## Updates
At the start of every run the plugin checks its source for a newer version and brings your Drive project up to date using the changelog. See `skills/partner-event-finder/prompts/00-update-check.md`. Install from a GitHub marketplace and turn on marketplace auto-update to get new versions automatically.

## What is inside

```
tejit-non-profit/
├── .claude-plugin/plugin.json
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
tejit-non-profit-claude/
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
