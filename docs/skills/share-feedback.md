# share-feedback

## What it does
Helps you tell the maintainer about a problem, an idea or something that could work better. It asks a few short questions, shows you the full message, and sends it only after you say yes. Please leave out donor details or other private information.

There are three ways it can reach the maintainer. If GitHub is connected, it files the report for you (public, including your email). If not, and you have a GitHub account, it gives you a link with the form already filled in and you click Submit. If you have no account, you can create a free one (the skill guides you) or send it by email instead. Email goes only to the maintainer and is not public. With Gmail connected it can send for you; otherwise it shows the email to copy, plus a mailto link.

Skill file: [skills/share-feedback/SKILL.md](../../skills/share-feedback/SKILL.md)

## Flow
```mermaid
flowchart TD
    A["Person says: share feedback or report a problem"] --> B["Short intro and a reminder not to include private details"]
    B --> C["Ask one question at a time: type, tool and goal, details, importance, example, email"]
    C --> D["Add the plugin version automatically"]
    D --> R{"GitHub tool or signed-in gh?"}
    R -- Yes --> E1["Draft for GitHub: This issue will be public, including your email"]
    R -- No --> Q{"Has a GitHub account?"}
    Q -- Yes --> E2["Draft for a pre-filled GitHub link, same public notice"]
    Q -- No --> P{"Create a free account or send by email?"}
    P -- Create account --> AG["Follow the account guide"] --> E2
    P -- Email --> E3["Draft for email: goes to the maintainer, not public"]
    E1 --> F{"Person says yes?"}
    E2 --> F
    E3 --> F
    F -- No --> G["Drop it kindly, nothing is sent"]
    F -- Yes --> H{"Route"}
    H -- GitHub tool --> I["File the report and show the link"]
    H -- GitHub link --> K["Give the pre-filled link, person clicks Submit"]
    H -- Email --> M{"Gmail connected?"}
    M -- Yes --> N["Send the email, or create a draft for the person to send"]
    M -- No --> O["Show the email to copy, plus a mailto link"]
    I --> L["Thank the person"]
    K --> L
    N --> L
    O --> L
```

## Use cases
- A staff member hits an error halfway through setup and wants it fixed.
- A volunteer thinks a step is confusing and suggests clearer wording.
- A team lead asks for a new helper, for example for volunteer scheduling.
