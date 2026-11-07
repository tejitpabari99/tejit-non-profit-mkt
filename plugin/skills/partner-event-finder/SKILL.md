---
name: partner-event-finder
description: Guided tool for nonprofits that finds where partner organizations announce fundraising events and keeps a shared Google Calendar of them current. Use when someone says "partner event finder", "set up the event finder", "find partner events", "collect events", "update the events calendar", or "find event sources". One skill handles first-time setup and every later run.
metadata:
  version: 0.1.2
  short_description: Finds partner fundraising events and adds them to a shared Google Calendar
  connectors: Google Drive, Google Sheets, Google Calendar, web search and page reading, GitHub (optional)
---

# Partner Event Finder (router)

Decide which phase applies, then read ONLY that phase's prompt file. Templates in `templates/` are the wording to use, filling in `<placeholders>`.

## Who you are talking to
Nonprofit staff who probably have never used an AI assistant, connectors or skills. Plain words, one question at a time, a suggested answer for every question. Reassure: nothing is shared or sent without their yes, events go only to the project calendar, and their original files are never changed.

## Always-on rules
1. **Formatting.** Every label (**Why:**, **What:**, **What I'll do:**, **Next:**, **Done:**) is **bold** and starts on its own new line, with a blank line between items. Never run labels together in one paragraph.
2. **High level only.** Say what is happening and why, in everyday words. NEVER show internal working to the person: no IDs, key or matching logic, column letters or numbers, schemas, file formats, tool or model names, batching mechanics. If a detail would make a nonprofit staffer ask "what does that mean?", leave it out. Simple facts are fine ("I found 7 organizations listed twice and combined them").
3. **Never edit the person's original sheet or document.** Read only. All writing goes to files this plugin created.
4. **Long explanations go in chat as a normal message, then ask a short follow-up question.**
5. **Explain every step** before and after (`templates/step-explainers.md`).
6. **Always end** with the closing statement in `templates/closing.md`.
7. **Always write a Log row** at the end of every run via `prompts/05-run-log.md`.
8. **Show links**: after creating or updating the folder or sheet, show the clickable link (`templates/folder-and-sheet-links.md`). When you reuse something that already exists (folder, sheet, calendar, memory), say so and give its link so they can click it.
9. Never delete anything. Never invent dates, times or venues.
10. **Work in small batches: at most 20 organizations at a time.** Never take more, even if asked for "all"; for "all", do consecutive batches of 20 (see `prompts/03-find-sources.md`).

## Which phase?
0. **Always first, quietly:** `prompts/00-update-check.md` (looks for a newer version and applies relevant changes before any task).
1. Look for the project: memory note first ("Partner Event Finder project ..."), else search Drive for the folder `tejit-np-plugin`, then `partner-event-finder`, then `metadata.txt` inside a project folder. If several projects, ask which.
2. **No project found, or the person asks to set up** → if the "about this skill" message was not shown yet in this conversation, send `templates/skill-about.md`, then `prompts/01-intro-and-permissions.md`, then `prompts/02-onboarding-setup.md`.
3. **Project exists** → read its `metadata.txt`, show a one-line status and suggest the best next step. A normal run is: find sources for a batch (`prompts/03-find-sources.md`), then add the events found to the project calendar (`prompts/04-collect-events.md`). That pair is one run. To refresh events for organizations that already have links, use `prompts/04-collect-events.md` alone.
4. After any phase, `prompts/05-run-log.md`, then `templates/closing.md`.

## Settings file
`metadata.txt` in the project folder (`key: value` lines, see `references/metadata-schema.md`). The Drive connector cannot change a file's contents in place: to change a setting, create a new `metadata.txt` in the same folder, then move the old one to Drive trash. Find it by folder plus name, never by a stored file ID.
