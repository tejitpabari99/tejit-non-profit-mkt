# Connections, per skill

Each skill only checks and asks for the connections it needs.

| Skill | Google Drive | Google Sheets | Google Calendar | Web search and page reading | GitHub | Gmail |
|---|---|---|---|---|---|---|
| `start` | not needed to read; used to save the source note | no | no | to check for a newer version (optional) | no | no |
| `partner-event-finder` | yes | yes | yes | yes | optional | no |
| `install-automation` | no | no | no | to fetch the latest guide | no | no |
| `share-feedback` | no | no | no | no | optional | optional |

**What they are used for (Partner Event Finder)**
- **Google Drive:** the `tejit-np-plugin` folder, small settings notes, finding your files.
- **Google Sheets:** reading your partner list (read only) and writing the new sheet this plugin creates.
- **Google Calendar:** the separate calendar where events are kept.
- **Web search and page reading:** reading partner websites.
- **GitHub (optional):** starring the project and sending feedback. With it, `share-feedback` files your report for you; without it you get a link and click Submit. A missing GitHub connection never blocks anything.
- **Gmail (optional):** `share-feedback` can send your feedback email for you if you choose the email route. Without it you get the finished email to copy and a link to open. A missing Gmail connection never blocks anything.

Google Docs is not needed. The plugin never edits your original spreadsheet or documents.
