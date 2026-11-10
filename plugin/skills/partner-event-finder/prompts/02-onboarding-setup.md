# Phase 2: onboarding setup

Use `templates/step-explainers.md` before and after each step. Suggest an answer for each question. Read `references/sheet-schema.md` and `references/metadata-schema.md` first (for yourself; never describe them to the person). Remember the high-level rule: no IDs, columns letters, matching logic or file formats in anything you say.

## Step 0: what already exists
Check memory and Drive for earlier work (project folder, sheet, calendar, notes). Whatever you find and will reuse, call out explicitly with its clickable link (`templates/folder-and-sheet-links.md`, "I found this already set up") so they can open it themselves. Reuse it instead of recreating it.

## Step 1: project folder
Explain, then create or reuse: `tejit-np-plugin` at the top of My Drive, inside it `partner-event-finder`, then the project folder. Say simply: "Next, we need to set up the project folder." Then ask: **"What should the project be called?"** with a suggestion based on the organization (for example `<organization>-partner-events`). Show the folder link.

## Step 2: partner list
Explain. Search Drive for sheets mentioning partner, directory, hub or list; show top matches with last-modified dates; suggest the best one. READ ONLY. Internally find the real header row and tab (ask which tab only if several are plausible).

## Step 3: read the list and confirm the data
Read only. Nothing is created or copied yet. Explain, then in this order:
1. Read the partner list.
2. **Confirm in plain words what will be used**, for example: "I'll use each partner's **name**, **website**, **category** and **city** from your list." (Only what exists; if there is no website column, say websites will be found for you and filled in as I go.) Show the first five organizations as they will appear and ask **"Does this look right?"** Do not mention column letters, IDs or matching.
3. Quietly work out how to recognise each organization (use `references/metadata-schema.md` "Recognising organizations"). If duplicates are found, say only, as a plan: "I found <N> organizations listed twice and will combine each pair into one."

## Step 4: categories
If the list has no category information, do not ask. Say: "Your list doesn't have categories, so I'll add one for each organization as I go." Then go to step 5.

Otherwise list the distinct categories with counts in a chat message, noting which likely do not host events. Then ask **"Which categories should be kept?"** with the categories as options and **"Keep all" as the LAST option** (suggested). Anything not chosen is left out of the new sheet (never removed from the original). Rows with no category stay. Only record the choice for now.

## Step 5: create the new sheet and copy
Only now, once the selection is final, create a new Google Sheet in the project folder named `<project name> sources` (separate from the original), with the tabs described in `references/sheet-schema.md`. Copy only the kept organizations into the Organizations tab (combining duplicate pairs), write in batches, and make Category a strict dropdown (see `references/sheet-schema.md`). Then, and only then, say "I added <N> organizations" and show the sheet link.

## Step 6: the calendar
Send `templates/calendar-instructions.md`, then ask the calendar name (suggest Partner Fundraising Events). Find it, confirm "Is this the one: <name>?", save it. Mention `guides/sharing-the-calendar.md`. No time-zone question.

## Step 7: defaults
Tell them (no decision needed): events tracked are galas, auctions, walks/runs, social fundraisers, giving campaigns and community events; the window is the next 12 months; each round does at most 20 organizations; the first run is a sample of 5. Ask only "any change?".

## Step 8: save your choices
Explain. Create `metadata.txt` in the project folder (plain text, no conversion to a Google file type) with the lines in `references/metadata-schema.md`, including `plugin_version`, `plugin_source`. Make sure the root `metadata.txt` also exists (`../../start/references/root-metadata.md`), including its `org`, `uid` and `consent_shown` lines from the identity check (`../../start/references/identity.md`); if the file exists without them, add them (create-new-then-trash-old). Read both back. Ask memory to remember: "Partner Event Finder project <name>: Drive folder `tejit-np-plugin/partner-event-finder/<name>`, settings file `metadata.txt`." If memory is unavailable, say so; the skill finds the folder by search.

## Step 9: finish setup and first run
Summarize in a few lines, show the folder and sheet links, log the run (`05-run-log.md`, phase `setup`). Ask: **"Shall we try a sample of 5 organizations now?"** If yes, go to `03-find-sources.md`.

## Changing settings later
Show what will change, get a yes, then create-new-and-trash-old for `metadata.txt`. Never delete anything else.

## If something fails
Say what failed in plain words, what was created so far, and offer to continue from there. Also offer to report it so it can be fixed: if they say yes, use the `share-feedback` skill (`../../share-feedback/SKILL.md`).
