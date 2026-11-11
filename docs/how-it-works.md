# How it works

## Repo layout
```
tejit-np-plugin/                   (repo root)
├── .claude-plugin/marketplace.json  marketplace file; points to plugin/
├── plugin/                        the plugin itself
│   ├── .claude-plugin/            plugin.json, icon.png
│   ├── gemini-extension.json      manifest for Gemini CLI
│   ├── skills/
│   │   ├── start/                 welcome, skills list, source record,
│   │   │                          optional GitHub step and account guide
│   │   ├── partner-event-finder/  SKILL.md router, prompts/, templates/,
│   │   │                          references/, scripts/
│   │   ├── install-automation/    SKILL.md, references/catalog.md
│   │   └── share-feedback/        SKILL.md, report format
│   ├── guides/                    short how-to pages for staff
│   ├── CHANGELOG.md, CONNECTORS.md
├── docs/                          these docs
├── scripts/build_zip.py           builds an upload ZIP
├── .github/                       CI checks, ISSUE_TEMPLATE/feedback.yml
├── LICENSE, README.md
```
The marketplace file stays at the repo root so marketplaces can find it; its `source` is `./plugin`. The plugin manifest lives in `plugin/.claude-plugin/` because Claude requires that folder. It is one copy, not a copy per tool. Other tools read the same `plugin/skills/` folder.

Each skill has a short `SKILL.md` that routes to numbered prompt files (loaded only when needed) and exact-wording templates.

## How updates work
- Installed copies update when the marketplace syncs and the version number in `plugin/.claude-plugin/plugin.json` is higher.
- Each time a skill runs, it checks the repo for a newer version and tells the person how to update with their tool.
- It then brings the person's saved project up to date using the "Project changes" in `plugin/CHANGELOG.md`.
- A plugin cannot replace its own files, so the person always does the update.

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

## Usage metrics and privacy
`start`, `partner-event-finder` and `install-automation` count their use anonymously. The first time you open any of them, they show one short note and ask for your organization's name (once). `share-feedback` never asks and never sends a count.

What is collected: tool and version, event type, test-or-real flag, organization name as typed (lowercased), a random code, counts, the failing step, the automation chosen, UTC time, a run code, and which AI or app sent it (a category only).

What is never collected: IP address, country, raw user-agent text, names, emails, partner lists, events, or file contents.

Where your identity is saved: in your AI assistant's memory when it has one, and in the root `metadata.txt` in your Drive folder `tejit-np-plugin` when Drive is already connected. With a saved identity you are never asked again. If neither is available, you are asked again next time.

A count is sent silently by one short web request, and a failed or blocked request never affects a run. See [TERMS.md](https://github.com/tejitpabari99/tejit-np-plugin/blob/main/TERMS.md) and [PRIVACY.md](https://github.com/tejitpabari99/tejit-np-plugin/blob/main/PRIVACY.md).

## Honest limits
It can only find what partners publish. Facebook and Instagram are not read in this version. It cannot create a calendar for you; the skill shows you how (one minute).
