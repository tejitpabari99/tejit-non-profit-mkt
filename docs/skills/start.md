# start

## What it does
The friendly front door. It explains in plain words what a plugin and a skill are, shows where the plugin came from, lists the helpers and the automations (using the same list as `install-automation`), and hands off to the one you pick. The first time, it also shows one short note about anonymous usage counts and asks for your organization's name (once; see [PRIVACY.md](https://github.com/tejitpabari99/tejit-np-plugin/blob/main/PRIVACY.md)). After you agree to the skill's access step, it saves a small note in Google Drive recording where the plugin came from.

Skill file: [plugin/skills/start/SKILL.md](../../plugin/skills/start/SKILL.md)

## Flow
```mermaid
flowchart TD
    A["Person says: Tejit's non profit tools"] --> B["Quiet check for a newer version"]
    B --> C["Welcome message: what a plugin and a skill are, where this came from"]
    C --> C2["First time only: short note and ask for the organization name"]
    C2 --> D["Show the list of skills"]
    D --> E["Ask which skill to set up"]
    E --> F["Hand off to the chosen skill"]
    F --> G["Person says yes to the skill's access step"]
    G --> H["Save a note in Google Drive about where the plugin came from"]
```

## Use cases
- A volunteer opens the tools for the first time and wants to know what is available.
- A staff member forgot the skill name and asks "what can you do?" later (answered by `install-automation`).
- A new user is asked for their organization's name once and never again.
- A team lead wants to see where the plugin came from before trusting it.
