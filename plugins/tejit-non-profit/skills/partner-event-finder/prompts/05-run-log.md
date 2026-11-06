# Run log (runs at the end of EVERY run)

Always add one row to the **Log** tab of the project sheet, even when the run found nothing, was stopped, or failed. This is required, not optional.

Columns: Date | Run ID | Session ID | Phase | Scope | Result counts | Issues

- Date: today, plain text `YYYY-MM-DD HH:MM`.
- Run ID: `R-` plus date and a short counter, e.g. `R-20261105-01`.
- Session ID: the current Claude session or conversation ID if you can get it (for example from the environment or session information available to you). If not available, write `not available`. Never invent one.
- Phase: `setup`, `find-sources` or `collect-events`.
- Scope: e.g. `sample 5`, `10 organizations`, `all remaining (308)`.
- Result counts: e.g. `5 checked, 3 event hosts, 7 links` or `4 added, 2 updated, 9 unchanged`.
- Issues: short text, or `none`.

Write all values as plain text. Mention in the report that the run was logged.
