# share-feedback

## What it does
Helps you tell the maintainer about a problem, an idea or something that could work better. It asks a few short questions, shows you the full message, and sends it only after you say yes. Reports are public, so it reminds you not to include donor details or other private information.

If GitHub is connected, it sends the report for you. If not, it gives you a link with the form already filled in, and you click Submit. A free GitHub account is needed for that last click, and the skill can guide you through making one.

Skill file: [skills/share-feedback/SKILL.md](../../skills/share-feedback/SKILL.md)

## Flow
```mermaid
flowchart TD
    A["Person says: share feedback or report a problem"] --> B["Short intro and a reminder not to include private details"]
    B --> C["Ask one question at a time: type, tool and goal, details, importance, example, email"]
    C --> D["Add the plugin version automatically"]
    D --> E["Show the full draft: This issue will be public, including your email"]
    E --> F{"Person says yes?"}
    F -- No --> G["Drop it kindly, nothing is sent"]
    F -- Yes --> H{"GitHub connected?"}
    H -- Yes --> I["File the report and show the link"]
    H -- No --> J["Offer help making a free account, then give a pre-filled link"]
    J --> K["Person reviews it and clicks Submit"]
    I --> L["Thank the person"]
    K --> L
```

## Use cases
- A staff member hits an error halfway through setup and wants it fixed.
- A volunteer thinks a step is confusing and suggests clearer wording.
- A team lead asks for a new helper, for example for volunteer scheduling.
