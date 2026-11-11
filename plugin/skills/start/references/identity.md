# Identity check (runs at the entry of `start`, `partner-event-finder` and `install-automation`)

Quiet and idempotent. Goal: know the person's organization (`org`), an anonymous random code (`uid`) and that the notice was shown (`consent_shown`). Run it once per conversation; with a saved identity it says nothing to the person at all.

Never mention pings, addresses, codes or ids to the person. The only things ever said are the notice and the question below.

## Steps
1. **Already known.** If `org`, `uid` and `consent_shown` are all known in this conversation, stop.
2. **Memory.** Read the memory note "Tejit's Non Profit Tools: identity" (keys `org`, `uid`, `consent_shown`). If all three are there, remember them for this conversation and stop. Do not read Drive.
3. **Drive (only if already available).** If the Drive tools are already loaded (never ask for them just for this), read the root `metadata.txt` in the Drive folder `tejit-np-plugin` (see `root-metadata.md`) and adopt any of `org`, `uid`, `consent_shown` that memory lacks. Write what you adopted back to the memory note. If memory and Drive disagree, memory wins and Drive is left alone.
4. **Fill what is still missing**, each piece on its own:
   - `consent_shown` missing and `org` missing: send ONE message, in this order, and nothing else (no extra explanation):

     > **Note:** The plugin collects anonymized usage metrics, for your organization (eg number of emails sent, or which step failed). No PII, or user data is collected. You can review the [Privacy Policy](https://github.com/tejitpabari99/tejit-np-plugin/blob/main/PRIVACY.md) and [Terms and Conditions](https://github.com/tejitpabari99/tejit-np-plugin/blob/main/TERMS.md) here.
     >
     > **Your organization's name?**

     This question has no suggested answer. The organization name is required.
   - `consent_shown` missing but `org` known (rare): send only the **Note:** line.
   - `org` missing but `consent_shown` known: send only the question.
   - Accept any non-empty text without checking it. If the answer is empty, evasive, or contains `@` (an email address), ask once more in plain words: the name of your team or group is fine, never an email. If there is still no usable answer, say kindly that the tools need an organization name to continue, and stop there.
   - Normalize `org`: trim, lowercase, each run of spaces becomes one `_`. Save and send it normalized.
   - `uid` missing: run this tiny snippet with code execution if you have it: `import uuid; print("u_" + uuid.uuid4().hex[:8])`. Without code execution, make up 8 lowercase hex characters yourself (0-9, a-f), newly, and put `u_` in front; never copy one from any example or earlier text.
   - Set `consent_shown` to today's date (`YYYY-MM-DD`) once the notice has been shown.
5. **Save.**
   - Memory note "Tejit's Non Profit Tools: identity" with `org`, `uid`, `consent_shown`.
   - Root `metadata.txt` keys `org`, `uid`, `consent_shown: <YYYY-MM-DD>`, only if Drive is already loaded and that file already exists (create-new-then-trash-old, keeping every other key, see `root-metadata.md`). Otherwise skip: the root `metadata.txt` is written later by `start` and by the partner-event-finder setup, which add these keys from the conversation.
   - Memory and Drive both unavailable: the identity lives for this conversation only. Say one plain line: "I can't remember this between chats here."
6. **Usage step (required, silent).** If a NEW `uid` was just generated in step 4, send the `setup_done` ping following `usage-ping.md` with `tool_name` = the skill that was entered (`start`, `partner-event-finder` or `install-automation`). This happens once per `uid`, whichever skill was opened first. Do it before moving on, so the turn does not end first.

## Later in the same conversation
Another of the three skills starting in the same conversation finds everything known (step 1) and says nothing.
