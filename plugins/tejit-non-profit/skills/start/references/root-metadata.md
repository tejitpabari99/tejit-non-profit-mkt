# Root `metadata.txt` (in Drive folder `tejit-non-profit-claude`)

Plain text, `key: value` lines. Records where this plugin came from. No secrets.

```
Tejit's Non Profit Tools: plugin settings
plugin: tejit-non-profit
plugin_source: https://github.com/<owner>/<repo>
plugin_marketplace: <marketplace name, if known>
plugin_version: 0.1.0
first_installed: 2026-01-01
last_checked: 2026-01-01
```

- Find it by folder plus name (`tejit-non-profit-claude` / `metadata.txt`), never by stored file ID.
- Create it if missing. If it exists, compare: when `plugin_source` or `plugin_version` differs, replace it.
- The Drive connector cannot edit a file's contents in place. To change it: create a new `metadata.txt` with the new lines, read it back, then move the old one to Drive trash. Never delete anything else.
- This is the "where it came from" record the update check reads (see `partner-event-finder/prompts/00-update-check.md`).
