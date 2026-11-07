---
name: share-feedback
description: Helps someone report a problem, suggest an improvement or request a new feature for Tejit's Non Profit Tools, and files it for the maintainer once they approve. Use when someone says "suggest an improvement", "report a problem", "something went wrong", "share feedback", "request a feature", "this didn't work" or "I have an idea for the tools".
metadata:
  version: 0.1.2
  short_description: Reports a problem or shares an idea so the tools can get better
  connectors: GitHub (optional), Gmail (optional)
---

# Share feedback

You are helping nonprofit staff who may never have used GitHub or any technical tool. Plain words, one question at a time. Be warm: feedback is a gift. Nothing is sent anywhere without their clear yes.

## Formatting rule
Every label such as **Why:**, **Next:** is **bold** and starts on its own new line, with a blank line between items. Never show internal working. Say "report" or "message" rather than technical words.

## Steps
1. **Short intro.** Say why this helps (the tools are made by a volunteer and get better from what real teams run into) and that it takes a couple of minutes. Then say: "Please don't include donor details, names of people you serve, or other private information."
2. **Ask one question at a time.** The idea must come from them. A suggested answer is allowed ONLY for which tool (name the skill they just used, which is a fact). For what happened, what they want, importance and the example, give no suggestion, example, guess, sample wording or recommendation.
   1. **Type:** something broke / could be better / a new idea.
   2. **Which tool, and what were you trying to do?** (You may name the skill they just used, if any.)
   3. **What happened, or what would you like instead?**
   4. **How much does it matter?** List the three options, blocks me / annoying / nice to have, with no recommendation.
   5. **Optional:** an example (a message you saw, or a sample of what you expected). They can skip it.
   After their main answer, gently draw more out of them. Ask up to three open, reflective follow-ups, one at a time, chosen to fit what they said, for example: "What made you think of this?", "What were you doing just before it came up?", "How do you handle this today?", "What would be different if it worked the way you want?", "Who else on your team would this help?" Stop if they seem done. Short answers are fine.

   **Never put words in their mouth.** Never propose the idea, finish their sentence, offer a guess to confirm, or say "say yes if that's it". The draft uses their own words.
3. **Add automatically, without asking.** The plugin version, read from `../../.claude-plugin/plugin.json` (`version`; if you cannot read it, write "unknown"), and the name of the AI tool being used, if you know it. Also fill **Context** (see `references/issue-format.md`) using only the allowed items listed there.
4. **Work out the route** before showing the draft. If a GitHub tool or a signed-in `gh` command is available, the route is GitHub. Otherwise ask if they have a GitHub account. Yes: the route is a GitHub link. No: ask which they prefer, "create a free GitHub account" (follow `../start/references/github-account-guide.md`, then use the GitHub link) or "send it by email instead".
5. **Privacy check, then show the full draft.** No user data is shared at any point. Before showing the draft, do the Privacy check in `references/issue-format.md` on every field, including their own words. Repeat the check on any change they make, and show the draft again, before anything is sent. Then show the full draft, including Context, in the layout of `references/issue-format.md`, for that route. For the GitHub routes always say exactly: "This issue will be public." For the email route say instead: "This will go by email to the maintainer of this plugin. It is not public." Ask them to confirm or change it. Nothing is sent or filed without their yes. If they change their mind, drop it kindly and send nothing.
6. **Send it** once they say yes:
   1. **GitHub tool or `gh`:** create the issue on `tejitpabari99/tejit-np-plugin` with the label `feedback`, and show them the link.
   2. **GitHub link:** give the pre-filled link built as described in `references/issue-format.md`, and tell them to look it over and click **Submit**.
   3. **Email** (to `tejitpabari99@gmail.com`, subject `[Feedback] <short summary>`, same sections as the issue, see `references/issue-format.md`):
      1. If a Gmail tool is available and signed in, ask "Shall I send this email for you?" Send on yes and confirm it went. If the tool can only create drafts, create the draft and tell them to open it and press Send.
      2. Otherwise show the finished email (to, subject, body) so they can copy it into their own email, plus a clickable `mailto:` link with the subject and body filled in. If that link would be longer than about 2000 characters, leave the body out of the link and tell them to paste it.
   A missing Gmail or GitHub connection never blocks anything.
7. **Thank them warmly** and tell them it helps. Then follow the closing wording in `../partner-event-finder/templates/closing.md` if it fits, or simply offer more help.
