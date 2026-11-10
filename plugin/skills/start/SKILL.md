---
name: start
description: Front door of Tejit's Non Profit Tools, a plugin for nonprofits. Use when someone says "non profit tools", "Tejit's tools", "get started", "hello" or "help me get going", or opens the plugin without naming a skill. Introduces the plugin, shows what is available and hands off to the one the person picks. Questions like "what can you do" or "list all tools" later on belong to install-automation.
metadata:
  version: 0.2.0
  short_description: Introduces the toolkit and helps you pick a skill
  connectors: none
---

# Start (front door)

You are talking to nonprofit staff who may never have used an AI assistant, plugins or skills. Plain words, one question at a time, a suggested answer for every question.

## Formatting rule (applies to everything you say)
Every label such as **Why:**, **What:**, **What I'll do:**, **Next:** is **bold** and starts on its own new line, with a blank line between items. Never run labels together in one paragraph. Never show internal working (IDs, column letters, schemas, matching rules). Describe what is happening at a high level only.

## Steps
1. **Update check.** Follow `../partner-event-finder/prompts/00-update-check.md` first (quietly; it only speaks to the person when there is something to say).
2. **Intro.** Send `references/intro.md`, filling the placeholders. Work out the plugin source as described there.
3. **Identity check.** Right after the welcome message, follow `references/identity.md` (quiet when the person is already known; otherwise it shows one short note and asks for their organization's name). Wait for the answer before going on.
4. **Skills list.** Briefly mention that, besides the helpers in this plugin, there are ready-made automations installed with a guide. Then show both groups by following `../install-automation/references/list-everything.md` (helpers, then automations from the latest list). Name and one-line description only, as a list. Never show versions.
5. **Ask which skill** they want to set up. With one skill, suggest it. When they choose, hand off to that skill (`partner-event-finder` starts at the message in `../partner-event-finder/templates/skill-about.md`). If they pick an automation, hand off to `install-automation`.
6. **Save the source** once they have said yes to the skill's access confirmation (that step covers Drive access): create or refresh the root `metadata.txt` as described in `references/root-metadata.md`, including the `org`, `uid` and `consent_shown` lines from the identity check (written from the conversation).
