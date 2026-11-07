# partner-event-finder

## What it does
You have a list of partner organizations. This skill visits their public websites, finds where they announce fundraising events (galas, auctions, walks and so on), saves the links in a Google Sheet, and adds the events to a separate Google Calendar your team can share.

It works in rounds of at most 20 organizations. The first run is a sample of 5. The first time, it also offers an optional extra: starring the project on GitHub (and helping you make a free account if you want one). It is optional. Events it finds are added straight to the separate project calendar, and it tells you what it added. Your original list is only read. Nothing is deleted.

Skill file: [plugin/skills/partner-event-finder/SKILL.md](../../plugin/skills/partner-event-finder/SKILL.md)

## Flow
```mermaid
flowchart TD
    A["Person asks to find partner events"] --> B["Quiet check for a newer version and project updates"]
    B --> C{"Existing project found?"}
    C -- No --> D["Explain what the skill does and wait for continue"]
    D --> E["Check Drive, Sheets, Calendar and web access, help turn on any that are missing"]
    E --> F["Confirm access with the person"]
    F --> F2["Optional, once: offer to star the project on GitHub, or help make a free account"]
    F2 --> G["Set up: project folder, partner list, confirm the data, categories, then create the new sheet and copy, calendar, defaults"]
    G --> H["Offer a sample of 5 organizations"]
    C -- Yes --> I["Show status and suggest the next step"]
    I --> J
    H --> J["Find sources: visit each website and save event links in the sheet"]
    J --> K["Look for events in the next 12 months"]
    K --> M["Add or update events in the separate calendar"]
    M --> O["Report what was added, with the sheet link"]
    O --> P["Add a row to the Log tab"]
    P --> Q["Offer 10 more, all remaining, or stop"]
```

## Use cases
- A development team wants to know which partner organizations are holding galas or auctions so staff can attend.
- A coalition tracks community fundraising walks across member organizations in one shared calendar.
- A volunteer refreshes the calendar every few months to catch newly announced dates.
- A board asks "what is coming up this year?" and gets a calendar to look at.
