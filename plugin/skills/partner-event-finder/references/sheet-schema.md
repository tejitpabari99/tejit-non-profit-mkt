# New sheet layout (created by this plugin; the original is never edited)

Stores organizations and saved event links only. Events live in the calendar.

**Organizations**: Org ID | Source Key | Name | Description | Website | Category | Triage | Sources status | Last checked | Notes
- Org ID: our own text ID, `ORG-001`... (plain text).
- **Source Key** (foreign key to the original sheet), always right after Org ID. Holds the original sheet's key value. If duplicate rows were merged, all original keys, separated by ` | `. Strength (strong/weak) is in `metadata.txt`.
- **Category** is a strict dropdown (data validation). It starts with the categories the person kept (empty if the original list had none) and grows as categories are added while finding sources, so it always holds every value used. Filled in while finding sources when blank; never overwrite one that is already there.
- **Description**: one short plain sentence about the organization, filled in while finding sources (blank if unclear). Sits right before Website.
- **Website**: copied from the original list when present; otherwise filled in while finding sources. Never overwrite one that is already there.
- Triage: `Event host`, `Not event host`, `No website`, `Unsure` (blank until checked).
- Sources status: `Not started`, `Done`, `Needs input`.

**Sources**: Source ID | Org ID | URL | Platform | Role | Status | Input needed | Last checked | Last result | Notes
- Platform: `Website`, `Eventbrite`, `Luma`, `GoFundMe Pro`, `Facebook`, `Instagram`, `Newsletter signup`, `PDF/flyer`, `Other`
- Role: `Primary` or `Supplementary`; Status: `Active`, `Needs input`, `Unreadable`, `Skipped` (Facebook/Instagram are recorded as Skipped).

**Log**: Date | Run ID | Session ID | Phase | Scope | Result counts | Issues. One row per run, always.

Write IDs, URLs and dates as plain text so the sheet does not convert them.
