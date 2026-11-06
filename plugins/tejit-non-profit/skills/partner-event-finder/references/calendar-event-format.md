# Calendar event format

**Title:** `[Organization] Event name (Type)`  Example: `[Example Org] Annual Gala (Gala)`
Types: Gala, Auction, Walk/Run, Social, Campaign, Community. Community events are open houses, tours and similar; they are not fundraisers.

**When**
- Date and time known: set start and end. Leave the time zone setting empty: Google then uses the user's own time zone. Only set it when the event states one (for example "6 pm ET") or its address is clearly in another region, using the matching IANA name.
- Only the date known: make it an all-day event and write "Time unconfirmed" in the description. Do not invent a time.
- Several days: one event spanning the days.
- End time unknown: use a two-hour block, and say "End time unconfirmed".

**Location:** venue and address if known.

**Notifications:** always send updates with notifications off.

**Description** has two parts separated by a marker line. Rewrite only the first part; copy the second part exactly as it is.

```
Source: <a href="EVENT_OR_PAGE_URL">EVENT_OR_PAGE_URL</a>
Platform: Website | Eventbrite | Luma | ...
Last verified: YYYY-MM-DD
Confidence: High | Medium | Low
Time unconfirmed.            (only when true)
Added automatically by Partner Event Finder.
----- STAFF NOTES (never changed automatically) -----
(write notes below this line)
```

Finding an existing event: list the events on the project calendar (never the primary calendar) with the source link as the search text; if nothing matches, search `[Organization]` within about 14 days either side of the date. Compare name, start, end and venue.
