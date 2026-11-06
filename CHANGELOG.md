# Changelog and version guidelines

## How to use this file (for the maintainer and for the assistant)

**Where versions live**
- Plugin version: `.claude-plugin/plugin.json` → `version` (the single source of truth; do NOT also set it in marketplace.json).
- Skill version: each skill's `SKILL.md` frontmatter → `metadata.version`. A skill's version changes only when that skill changes.
- A project's last applied version: `plugin_version` in the project's `metadata.txt` in Drive.

**Numbering (semantic versioning, 0.x while testing)**
- PATCH (0.1.0 → 0.1.1): wording and bug fixes. No project changes.
- MINOR (0.1.x → 0.2.0): new or changed behaviour, new skill, or any change that needs existing projects updated.
- MAJOR (→ 1.0.0): first official release, or a breaking change.

**Every release, in this order**
1. Add a section below, newest first, headed `## <version> (<date>)`.
2. Fill the three parts: **What's new for users** (everyday words), **Project changes** (exact steps the assistant performs on an existing Drive project; "none" if none), **Maintainer notes**.
3. Bump `plugin.json` version and the changed skills' `metadata.version`. Without a new version number, installed copies will NOT update.
4. Validate the plugin, commit, push.

**What the assistant does at the start of every run** (`prompts/00-update-check.md`): compares the project's `plugin_version` with the installed version, reads every section newer than the project's version (oldest first), performs the **Project changes** relevant to the skill being used, then updates `plugin_version`. Write Project changes as precise, safe, repeatable steps. Never include deleting user data.

---

## 0.1.0 (2026-11-05)

First release of Tejit's Non Profit Tools.

**What's new for users**
- A friendly welcome that explains what a plugin and a skill are, where this plugin came from, and lists the available skills.
- Partner Event Finder: finds where your partner organizations announce fundraising events, saves the links in a Google Sheet, and adds the events to a shared Google Calendar after you say yes.
- Each organization in your sheet gets a short description and a website as the tool visits it.
- Work is done in small rounds (at most 20 organizations at a time).
- The tool checks for a newer version each time it starts and brings your project up to date.
- An optional, one-time offer to star the project on GitHub, with a step-by-step guide to making a free account if you want one. You can skip it.
- Share Feedback: report a problem or share an idea in a couple of minutes. You see the full message first, and nothing is sent without your yes.

**Project changes** (apply to projects created by test builds before 0.1.0, i.e. no `plugin_version` in their `metadata.txt`)
1. In the project sheet's Organizations tab, if there is no **Description** column, insert one directly before **Website** (leave blank; it fills in as organizations are visited).
2. Fill **Website** from the original list where it is empty and a web address is known; never overwrite existing values.
3. Make sure the root Drive folder `tejit-np-plugin` contains a `metadata.txt` recording the plugin source and version (create it if missing).
4. Add `plugin_version: 0.1.0` and `plugin_source` to the project `metadata.txt`.

**Maintainer notes**
- Version kept at 0.1.0 because the plugin is not yet published.
- Skills: `start` 0.1.0, `partner-event-finder` 0.1.0, `share-feedback` 0.1.0.
- Added the feedback form `.github/ISSUE_TEMPLATE/feedback.yml` and the `feedback` label. Root `metadata.txt` may now hold `github_step: done`.
- The CI version-bump check does not apply to this change because `main` has no `plugin.json` yet.
