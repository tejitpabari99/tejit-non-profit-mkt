# How it works

## Repo layout
```
tejit-np-plugin/                   (repo root = the plugin)
├── .claude-plugin/                plugin.json, marketplace.json, icon.png
├── gemini-extension.json          manifest for Gemini CLI
├── skills/
│   ├── start/                     welcome, skills list, source record,
│   │                              optional GitHub step and account guide
│   ├── partner-event-finder/      SKILL.md router, prompts/, templates/,
│   │                              references/, scripts/
│   └── share-feedback/            SKILL.md, report format
├── guides/                        short how-to pages for staff
├── docs/                          these docs
├── scripts/build_zip.py           builds an upload ZIP
├── .github/                       CI checks, ISSUE_TEMPLATE/feedback.yml
├── CHANGELOG.md, CONNECTORS.md, LICENSE, README.md
```
The manifest lives in `.claude-plugin/` because Claude requires that folder. It is one copy, not a copy per tool. Other tools read the same `skills/` folder.

Each skill has a short `SKILL.md` that routes to numbered prompt files (loaded only when needed) and exact-wording templates.

## How updates work
- Installed copies update when the marketplace syncs and the version number in `.claude-plugin/plugin.json` is higher.
- Each time a skill runs, it checks the repo for a newer version and tells the person how to update with their tool.
- It then brings the person's saved project up to date using the "Project changes" in `CHANGELOG.md`.
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

## Honest limits
It can only find what partners publish. Facebook and Instagram are not read in this version. It cannot create a calendar for you; the skill shows you how (one minute).
