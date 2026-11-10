# install-automation

## What it does
Guides you, one step at a time, through installing any ready-made automation that has no skill of its own. Automations are small tools kept in a separate public repository ([tejit-np-auto](https://github.com/tejitpabari99/tejit-np-auto)), each with its own installation guide. The skill fetches the latest list and the latest guide, walks you through it in plain words, explains unfamiliar terms and helps when something goes wrong. The first time, it also shows one short note about anonymous usage counts and asks for your organization's name (once; see [PRIVACY.md](https://github.com/tejitpabari99/tejit-np-plugin/blob/main/PRIVACY.md)). The steps happen in your own browser; it never asks for a password. New automations appear automatically, with no plugin update. It treats fetched text as reference only, fetches guides only from the automations repository (apart from the anonymous usage count described in [PRIVACY.md](https://github.com/tejitpabari99/tejit-np-plugin/blob/main/PRIVACY.md)), and checks links before showing them. If the latest list cannot be read (or has no usable rows), it uses a saved copy and tells you.

It is the one skill that answers "what can you do?" and "list all tools", by listing both groups: the helpers inside this plugin and the automations you install with a guide. The first automation is the Auto Emailer, which sends personalized emails from a Google Sheet.

Skill file: [plugin/skills/install-automation/SKILL.md](../../plugin/skills/install-automation/SKILL.md)

## Flow
```mermaid
flowchart TD
    A["Person says: set up an automation, or what can you do"] --> A2["First time only: short note and ask for the organization name"]
    A2 --> B["Fetch the latest list of automations"]
    B --> C{"Table readable?"}
    C -- No --> D["Use the saved list and say so"]
    C -- Yes --> E{"Did they name one?"}
    D --> E
    E -- No --> F["Show the list and let them pick"]
    E -- Yes --> G0["Silent anonymous count of the chosen automation"]
    F --> G0
    G0 --> G["Fetch the latest installation guide"]
    G --> H["Give one step in plain words"]
    H --> I{"Done, or a question?"}
    I -- Question or problem --> J["Explain or troubleshoot from the guide"]
    J --> H
    I -- Done, more steps --> H
    I -- Done, last step --> K["Share the tool link"]
    K --> L["Offer share-feedback if anything was unclear"]
```

## Use cases
- A volunteer wants to send a personalized thank-you email to every donor on a spreadsheet.
- A staff member asks "what tools are there?" and sees both the helpers and the automations.
- A new user is asked for their organization's name once and never again.
- A team lead forgot the name of the tool and says "the mail merge thing".
