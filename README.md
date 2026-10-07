# ⚡ Save Restricted Content Downloader Bot
### 🚀 Developed & Maintained by [@sheffysamra1bot](https://t.me/sheffysamra1bot)
> **Official Support & Updates:** [https://t.me/sheffysamra1bot](https://t.me/sheffysamra1bot)

---

An ultra-fast, military-grade secured Telegram **Save Restricted Content Downloader** built with **Pyrofork**, **TgCrypto**, **Fernet AES-256 Encryption**, and **MongoDB**. Designed to download, bypass, and transfer restricted media, videos, photos, documents, and messages directly across Private Chats, Groups, Channels, and Topic Supergroups.

---

## 🚀 One-Click Heroku Deployment

Click the button below to directly deploy this repository to Heroku using the pre-configured `app.json` (Pre-set with `standard-2x` dyno and pre-filled configuration variables).

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/sheffykhlg/src-4)

---

## 🔥 Key Features

* **Save Restricted Content Downloader:** Seamlessly downloads and bypasses restricted channel/group content without restrictions.
* **Military-Grade AES-256 Session Encryption:** Telegram string sessions are encrypted via Fernet AES-256 before being stored into MongoDB. No plain sessions are saved!
* **Aria2c Turbo Speed Engine:** Multi-connection parallel media downloader daemon for peak transfer speeds.
* **Modular Configuration Architecture (`configs.py`):** Clean environment variable management with dummy placeholders for effortless deployment.
* **Preserved Media Attributes:** Keeps original captions, high-resolution thumbnails, video duration, height, width, and streaming properties.
* **Context-Aware Uploads:** Automatically uploads content in PM, Group, Channel, or Specific Topic Supergroups depending on where the command was issued.
* **Zero FloodWait Anti-Flood Protection:** Throttled status message updates (8-second intervals) to eliminate Telegram `429 FloodWait` limits.
* **Interactive Batch Processing:** Built-in interactive `/batch` wizard with custom range selection.
* **Custom Word & Link Filter:** Auto-removes external links and replaces custom words via `/replace`.
* **Cryptographic Anti-Leech Protection:** Built-in integrity engine ensuring developer attribution remains intact.
* **Force Cancel Support:** Instant task termination using `/forcecancel` or `/cancel`.

---

## 🛠️ Bot Commands Menu

| Command | Description |
| :--- | :--- |
| `/start` | Welcome guide and command overview |
| `/addsession` | Bind Pyrogram String Session to your account (Encrypted in DB) |
| `/replace` | Set word replacement rules and link filters |
| `/delsession` | Remove your saved session from MongoDB |
| `/batch` | Start range-based batch download wizard |
| `/forcecancel` | Abort ongoing downloads and batch prompts immediately |
| `/stats` | View live database session counts and disk usage |
| `/cancel` | Cancel active text prompts |

---

## ⚙️ Environment Variables Config

| Variable | Description | Example / Default |
| :--- | :--- | :--- |
| `API_ID` | Telegram API ID from my.telegram.org | `12345678` |
| `API_HASH` | Telegram API Hash from my.telegram.org | `0123456789abcdef0123456789abcdef` |
| `BOT_TOKEN` | Telegram Bot Token from @BotFather | `1234567890:ABCdef...` |
| `MONGO_URI` | MongoDB Atlas Connection URL | `mongodb+srv://...` |
| `ENCRYPTION_KEY` | Custom AES Secret Key (Optional) | `Auto-generated / Pre-set` |
| `LOG_GROUP_ID` | Telegram Log Group ID (Optional) | `-1001234567890` |
| `LOG_CHANNEL_ID` | Telegram Log Channel ID (Optional) | `-1009876543210` |

---

## 📂 Project Structure

```text
├── Procfile             # Heroku process declaration (worker: python main.py)
├── app.json             # Heroku deploy specifications (standard-2x plan)
├── configs.py           # Configuration & AES-256 Encryption Engine (@sheffysamra1bot)
├── main.py              # Save Restricted Content Downloader Engine (By @sheffysamra1bot)
├── README.md            # Repository documentation with Deploy Button
├── requirements.txt     # Python Dependencies
└── runtime.txt          # Python Runtime Version (3.10.10)
```

---

## 👑 Credits & Author
- **Developer & Creator:** [@sheffysamra1bot](https://t.me/sheffysamra1bot)
- **Telegram Channel / Updates:** [https://t.me/sheffysamra1bot](https://t.me/sheffysamra1bot)
- **Official GitHub Repo:** [https://github.com/sheffykhlg/src-4](https://github.com/sheffykhlg/src-4)
- **License / Attribution Notice:** Developed and maintained by [@sheffysamra1bot](https://t.me/sheffysamra1bot). All modifications, forks, or deployments must retain attribution to the original author.

