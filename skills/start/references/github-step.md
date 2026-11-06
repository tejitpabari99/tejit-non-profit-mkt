# Optional GitHub step (runs once per person)

Shared by every skill. A skill's intro prompt points here after access is confirmed. Always label it **(optional)** when you speak to the person. Never block on it, never push, never star without a clear yes.

## Skip it if already done
Check the root `metadata.txt` (`root-metadata.md`) for `github_step: done`, and memory for a note like "GitHub step done". If either says done, skip this whole file.

## Say first (plain words)
> **(optional)** One quick extra before we start. This project is open, which means you can read how it works at any time, and you can ask for improvements. Staying connected on GitHub is a nice way to do that.

## Flow
1. **Quietly check.** If a GitHub tool is loaded, or a signed-in `gh` command works, check whether the person is signed in. Say nothing technical about the check.
2. **Signed in, or they say they have an account.** Go to the star prompt (step 5).
3. **Cannot tell.** Ask: "**(optional)** Do you have a GitHub account?" Options: Yes / No / Skip. Suggest Skip if they seem unsure. Yes goes to step 5. No goes to step 4. Skip goes to step 6.
4. **No account.** Say: "**(optional)** I recommend creating a free GitHub account to keep track of changes to this plugin, see new versions, and give feedback. It is optional and takes about a minute. Would you like to do that?"
   - Yes: follow `github-account-guide.md`, one step at a time, and wait until they say they are done. Then go to step 5.
   - No: reply warmly ("No problem at all, you can do it any time.") and go to step 6.
5. **Star prompt.** Say: "**(optional)** Would you like to star this project on GitHub? It saves the project to your account so you can keep track of changes, new versions, and give feedback. Say yes and I'll do it, or skip it."
   - Yes, and you have a tool that can star: star `https://github.com/tejitpabari99/tejit-np-plugin`, then confirm it is done.
   - Yes, and you have no such tool: give the link `https://github.com/tejitpabari99/tejit-np-plugin` and say to click the **Star** button near the top right.
   - Skip or no: move on warmly.
   - Never star without a clear yes. Never say a star gives automatic updates: starring does not update the plugin.
6. **Record it.** Whatever they chose (yes, no or skip), do not ask again. Add `github_step: done` to the root `metadata.txt`, using the create-new-then-trash-old rule in `root-metadata.md`. If memory is available, also save a note: "GitHub step done." If neither can be written, just carry on.
7. Continue with the skill.
