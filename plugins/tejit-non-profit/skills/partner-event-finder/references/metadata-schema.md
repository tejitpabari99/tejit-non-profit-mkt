# Settings file: `metadata.txt`

Plain text file in the project folder, created by setup. Nobody needs to edit it. No passwords or secrets, only IDs and choices. Run history is in the sheet's Log tab.

```
Partner Event Finder: project settings (tejit-non-profit plugin)
schema_version: 3
plugin_version: 0.1.0
plugin_source: https://github.com/<owner>/<repo>
plugin: tejit-non-profit
skill: partner-event-finder
project_name: Example Partner Events
created: 2026-01-01
main_folder_name: tejit-non-profit-claude
main_folder_id:
skill_folder_id:
project_folder_id:
input_sheet_id:
input_tab: Sheet1
input_header_row: 2
input_column_name: B
input_column_website: E
input_column_category: C
input_column_city: K
fk_source_column: A
fk_strength: strong
kept_categories: Example Category | Another Category
output_sheet_id:
calendar_id:
calendar_name: Partner Fundraising Events
window_months: 12
event_types: Gala | Auction | Walk/Run | Social | Campaign | Community
setup_complete: true
```

**Version fields.** `plugin_version` is the plugin version this project was last brought up to date with (the update check compares it with the installed version and the CHANGELOG). `plugin_source` is where the plugin came from.

**Recognising organizations (internal, never explain to the person).** `fk_source_column` is the column of the original sheet used to link back to it. `fk_strength: strong` = a real unique ID column, so deduplicate and re-match directly by exact key. `fk_strength: weak` = a stand-in (name or website), so match loosely: ignore case, spelling, punctuation, "Inc."/"The", www; use judgment, ask when unsure. Our own `Org ID` is separate; the key is copied into the sheet's Source Key column.

**Reading:** open with the Drive text reader. **Finding:** by folder and name (`metadata.txt` inside the project folder), not by stored file ID.
**Changing a setting:** Drive connectors cannot change a file's content in place. Create a new `metadata.txt` with the updated lines, verify by reading it back, then move the old one to Drive trash. Because lookup is by folder and name, nothing breaks. Never delete anything else.
