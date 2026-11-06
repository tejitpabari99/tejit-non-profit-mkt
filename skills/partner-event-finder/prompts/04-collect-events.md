# Phase 4: collect events (second half of a run, or a refresh on its own)

Read `references/calendar-event-format.md`, `references/sheet-schema.md`, and `metadata.txt`. Use only the project calendar named in metadata, never the primary calendar.

1. **Scope.** After `03-find-sources.md`: the organizations just done (at most 20). On its own (refresh): organizations with Active sources, oldest "Last checked" first, at most 20.
2. **Look for events** per organization (two at a time, small fast model for extraction when available):
   - Read each Active source, follow links one level, skip Facebook/Instagram.
   - Extract events in the window (`window_months`): name, type, start, end, time zone only if stated, venue, link, confidence. Drop past events. Never treat last year's date as this year's; report "no new date announced".
   - Compare with existing calendar events per the format file to decide add, update, or leave alone. Unsure = collect a question, write nothing. Never delete.
3. **Ask before adding (required).** Show the events found and ask explicitly "Should I add them to your calendar?" using `templates/run-flow.md`. Write nothing to the calendar until they say yes. If they said earlier to add automatically for "do all", you may add without asking each round, but still report each round.
4. **Add/update** after the yes. On update rewrite only the part above the STAFF NOTES line and keep the rest exactly. Notifications off. Update each source's Last checked and Last result.
5. Ask any collected questions together, one at a time, with a suggested answer.
6. **Report** in everyday words: added, updated (each "was ... now ..."), unchanged, answered, sources that could not be read. Name the calendar and offer `guides/sharing-the-calendar.md`. Show the sheet link (every time). **This completes one run.**
7. Run `05-run-log.md` (phase `find-sources` + `collect-events`), then offer what next (see "What next" in `templates/run-flow.md`) and end with `templates/closing.md`.
