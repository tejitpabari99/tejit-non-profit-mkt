# Phase 3: find sources (first half of a run)

Read `references/sheet-schema.md` and the project `metadata.txt` first. Read the project sheet. Never touch the original sheet. Remember the formatting and high-level rules in SKILL.md.

1. **Status** in one line ("320 organizations, 12 done, 308 to go").
2. **Pick a batch** of organizations whose sources are Not started. Size: 5 on the very first run (`templates/run-flow.md`), otherwise what the person chose, **never more than 20**. If they ask for "all", do successive batches of 20 as described in `templates/run-flow.md`.
3. **For each organization** (two at a time; use a small fast sub-agent for narrow steps if available):
   - **Triage:** Event host / Not event host / No website / Unsure, one-line reason. Settle Unsure with a stronger model or ask the person.
   - **Discover** (Event hosts only): home page, events or news page, one level of links to event platforms (Eventbrite, Luma, GoFundMe Pro), flyers/PDFs, newsletter signup; one web search for third-party listings. Confirm each link belongs to this organization. Label Platform and Role.
   - **Fill in the organization row while you are there:** a **Description** (one short plain sentence about what the organization does, from its own website; leave blank if unclear) and the **Website** (the organization's main address) when the sheet's Website is empty. Never overwrite an existing Website; if you find a different one, put it in Notes.
   - **Category:** also fill a blank Category (when the original list had none, and for blank rows when it had some). Reuse an existing dropdown value when it fits. If none fits, first add a short plain new value to the dropdown, then write it, so the strict dropdown always holds every value. Never overwrite a Category already filled. A category added this way never removes the organization.
   - **Facebook/Instagram:** record as Skipped.
   - **Write:** Sources rows (same organization and URL = update, never duplicate); set Triage, Sources status, Last checked.
   - A page that needs login or can't be read: Needs input or Unreadable, with why. Never count it as "no events".
4. **Report** in plain words: how many checked, how many host events, links saved, items needing help (exact link and what to do). Show the sheet link (every time).
5. **Continue straight to `04-collect-events.md`** for this same batch. The run is not complete until the person has been asked about adding events to the calendar. Do not offer "10 more" before that.

Rules: never delete rows; do not guess, mark Unsure; if a limit is hit say where you stopped (the sheet shows what is done).
