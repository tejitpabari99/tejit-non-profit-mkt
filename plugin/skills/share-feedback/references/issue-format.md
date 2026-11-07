# Feedback report format

## Title
`[Feedback] <short summary>` (a few words, in the person's own terms).

## Body (exact sections, in this order)
These match the fields of the form `.github/ISSUE_TEMPLATE/feedback.yml`.

```
### Feedback type
<something broke | could be better | new idea>

### Tool and goal
<which tool, and what they were trying to do>

### Details
<what happened, or what they would like instead>

### Importance
<blocks me | annoying | nice to have>

### Example
<their example, or "none">

### Context
<filled in by the assistant, see below>

### Plugin version
<version from the plugin manifest, plus the AI tool name if known>
```

Label: `feedback`.

## Context (filled in without asking)
Allowed items only: which skill; which step or phase they were on; whether it was setup, a first run or a repeat run; what kind of action was happening, in general terms; the kind of problem, in general terms; which connections were available (Drive, Sheets, Calendar, web). Example: "Partner Event Finder, repeat run, collecting events; Drive, Sheets and Calendar connected."

Never include: names of organizations, partners, people or projects; emails; links; file, sheet, folder or calendar names; IDs; event details; numbers from their data; anything pasted from their files.

## Privacy
No user data is shared at any point. Before showing the draft, check every field, including their own words, and replace anything on the Never include list above with a general description (for example "a partner organization"). Tell them you replaced it, and what you replaced it with in general terms. Repeat this check on any change they make, and show the draft again before anything is sent.

## Creating it directly
When a GitHub tool or signed-in `gh` command is available, create the report on `tejitpabari99/tejit-np-plugin` with the title and body above and the label `feedback`. Show the link it returns.

## Pre-filled link (no tool available)
```
https://github.com/tejitpabari99/tejit-np-plugin/issues/new?template=feedback.yml&title=<urlencoded>&feedback_type=<urlencoded>&tool_goal=<urlencoded>&details=<urlencoded>&importance=<urlencoded>&example=<urlencoded>&context=<urlencoded>&version=<urlencoded>
```
- Percent-encode every value (spaces as `%20`, new lines as `%0A`).
- `title` is the full title, including `[Feedback] `.
- Always include `feedback_type`, with exactly one of: something broke | could be better | new idea. (The field id is `feedback_type` because `type` clashes with GitHub's own issue type and is not filled in.)
- Do NOT add a `labels=` parameter. The form applies the label itself.
- If the whole link would be longer than about 6000 characters, shorten the example text. If it is still too long, tell them to open `https://github.com/tejitpabari99/tejit-np-plugin/issues/new?template=feedback.yml` (the plain form) and paste in the answers you show them.
- Tell them to review the form and click **Submit**. Remind them it will be public.

## Email route
Used when the person has no GitHub account and prefers email.
- To: `tejitpabari99@gmail.com`
- Subject: the same title, `[Feedback] <short summary>`.
- Body: the same sections as above, in the same order, as plain text.
- With a Gmail tool signed in: send it after their yes, or create a draft if the tool can only draft, and tell them to open it and press Send.
- Without one: show to, subject and body to copy, plus a link:
```
mailto:tejitpabari99@gmail.com?subject=<urlencoded>&body=<urlencoded>
```
  Percent-encode both values (spaces as `%20`, new lines as `%0A`). If the whole link would be longer than about 2000 characters, leave out `body=` and tell them to paste the body shown.
- Remind them it goes only to the maintainer and is not public. Their address is simply the sender.
