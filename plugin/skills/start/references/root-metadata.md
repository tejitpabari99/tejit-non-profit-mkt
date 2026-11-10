# Root `metadata.txt` (in Drive folder `tejit-np-plugin`)

Plain text, `key: value` lines. Records where this plugin came from. No secrets.

```
Tejit's Non Profit Tools: plugin settings
plugin: tejit-np-plugin
plugin_source: https://github.com/<owner>/<repo>
plugin_marketplace: <marketplace name, if known>
plugin_version: 0.1.0
first_installed: 2026-01-01
last_checked: 2026-01-01
github_step: done
org: red_cross
uid: u_<8 hex>
consent_shown: 2026-01-01
```

- Find it by folder plus name (`tejit-np-plugin` / `metadata.txt`), never by stored file ID.
- Create it if missing. If it exists, compare: when `plugin_source` or `plugin_version` differs, replace it.
- The Drive connector cannot edit a file's contents in place. To change it: create a new `metadata.txt` with the new lines, read it back, then move the old one to Drive trash. Never delete anything else.
- `github_step: done` is added once the person has been through (or skipped) the optional GitHub step (`github-step.md`). Leave the line out until then. Keep it when refreshing the file. Same create-new-then-trash-old rule.
- `org`, `uid` and `consent_shown` are written by the identity check (`identity.md`) and from the conversation when this file is created. Every rewrite of this file keeps all three exactly as they are. Leave them out only while unknown. The `uid` shown above is a placeholder, never copy it.
- This is the "where it came from" record the update check reads (see `partner-event-finder/prompts/00-update-check.md`).
