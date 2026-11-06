# Publishing Tejit's Non Profit Tools on GitHub (as a plugin marketplace)

Checked against Anthropic's plugin docs (code.claude.com/docs/en/plugins, plugin marketplaces, discover-plugins) on 2026-11-05.

## What goes in the repo
Use the ready folder `marketplace-repo/` (also zipped as `tejit-non-profit-marketplace.zip`). It passed `claude plugin validate`.

```
tejit-non-profit-marketplace/            <- the GitHub repo root
├── .claude-plugin/marketplace.json      <- required; lists your plugins
├── README.md                            <- install instructions for users
└── plugins/
    └── tejit-non-profit/                <- the plugin itself
        ├── .claude-plugin/plugin.json
        ├── CHANGELOG.md
        └── skills/ ...
```
`marketplace.json` has `name`, `owner`, and a `plugins` list; each entry has `name` and `source: "./plugins/tejit-non-profit"`. The entry name must match `plugin.json`'s name.

## Steps
1. On github.com click **New repository**. Name it `tejit-non-profit-marketplace` (if you pick another name, change it in `plugin.json` `homepage` and `repository`, and in the READMEs). Public is simplest (free, no sign-in for users). Leave it empty.
2. Unzip `tejit-non-profit-marketplace.zip`, then in that folder:
   ```
   git init -b main
   git add .
   git commit -m "Tejit's Non Profit Tools 0.1.0"
   git remote add origin https://github.com/tejitpabari99/tejit-non-profit-marketplace.git
   git push -u origin main
   ```
   (Or use GitHub's **Add file > Upload files** and drag the folder contents in, keeping the `.claude-plugin` folder.)
3. Test it yourself in Claude Code:
   ```
   /plugin marketplace add tejitpabari99/tejit-non-profit-marketplace
   /plugin install tejit-non-profit@tejit-non-profit-marketplace
   ```
   Then say "Tejit's non profit tools".
4. Turn on auto-update: `/plugin` > **Marketplaces** > your marketplace > **Enable auto-update**. Third-party marketplaces have it OFF by default, so each nonprofit user must switch it on once. Manual update any time: `/plugin marketplace update tejit-non-profit-marketplace`.
5. Share the two install lines (or the repo link) with nonprofits. The Claude desktop/web app: the docs I read describe adding a GitHub marketplace in Claude Code (CLI, desktop Code tab, VS Code). I did not find a documented "add GitHub marketplace" button for the regular chat or Cowork. For those, use a Team/Enterprise organization upload (Organization settings > Plugins & skills, needs a private or internal GitHub repo) or the `.plugin` file.

## Releasing a new version (important)
1. Edit the plugin, add a section to `CHANGELOG.md`, bump `version` in `plugin.json` (and the changed skill's `metadata.version`).
2. Commit and push to `main`.
3. If you do NOT bump the version, users will not receive the change (docs: pushing without changing `version` is invisible to them).
4. At the start of each run, the skill checks the repo for a newer version, tells the person how to update, and applies the CHANGELOG "Project changes" to their Drive project. A plugin cannot replace its own files, so the actual update happens through the marketplace update (auto-update, or `/plugin marketplace update`).

## Good to know
- Version lives only in `plugin.json`; do not also set it in `marketplace.json`.
- Private repo: works only for people whose computer is signed in to GitHub with access (credential helper / `gh auth login`). A public repo avoids this for nonprofits.
- Optional: add a square PNG icon (512 to 2048 px) at `.claude-plugin/icon.png`; the validator only advises.
- Not covered by what I checked: the official directory submission and Cowork UI details.
