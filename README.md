

# 🚀 Alpha Userbot (Beta Version)

**Alpha Userbot** is a powerful userbot built using **Pyrogram** V2, designed to make Telegram automation easier. It includes features like muting, banning, spamming, raiding, and much more. The bot is currently in **Beta Version**, so new features and improvements are on the way! 🎉

## 🌟 Features

- 🔔 **Ping**: Check the bot's status and uptime with `.ping`
- 🛑 **Mute / Unmute**: Mute and unmute users by username using `.mute @username` and `.unmute @username`
- 🚫 **Ban / Unban**: Ban and unban users using `.ban @username` and `.unban @username`
- 👢 **Kick**: Kick users from the chat using `.kick @username`
- ⚙️ **Promote / Demote**: Promote and demote users using `.promote @username` and `.demote @username`
- 🔥 **Spam**: Spam a message multiple times with `.spam <number_of_times> <message>`
- 💥 **Raid**: Launch a raid of abusive messages with `.raid <username> <number_of_raids>`
- ⏹️ **Stop Spam / Raid**: Stop spamming or raiding with `.sspam` and `.draid`
- 🆘 **Help**: Use `.help` to see all available commands and how to use them.

## 🛠️ How to Deploy on Termux

Follow these steps to deploy **Alpha Userbot** on **Termux**.

### 1. Install Termux

- Download and install **Termux** from [Google Play Store](https://play.google.com/store/apps/details?id=com.termux) or [F-Droid](https://f-droid.org/en/packages/com.termux/).

### 2. Update and Install Dependencies

Open Termux and run these commands to update and install necessary packages:

```bash
pkg update && pkg upgrade
pkg install python git -y

3. Clone the Bot Repository

Clone the bot repository from GitHub:

git clone https://github.com/yourusername/alpha-userbot.git
cd alpha-userbot

4. Install Required Python Libraries

Install the required libraries by running:

pip install -r requirements.txt

5. Generate Pyrogram V2 Session String

Create a session string to authenticate your bot:

1. Create a Python script to generate the session:



nano generate_session.py

2. Add the following content:



from pyrogram import Client

api_id = 1234567  # Replace with your API ID
api_hash = "your_api_hash"  # Replace with your API Hash

with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
    print(app.export_session_string())

3. Run the script:



python generate_session.py

4. Copy the generated session string.



6. Configure the Bot

Edit main.py and update your API ID, API hash, and session string:

api_id = 1234567  # Your API ID
api_hash = "your_api_hash"  # Your API Hash
string_session = "your_string_session"  # Your Session String

7. Run the Bot

Run the bot using:

python main.py

Your Alpha Userbot should now be live and working in Termux! 🎉

8. Keep the Bot Running in Background (Optional)

Use tmux to keep the bot running even when you close Termux:

pkg install tmux
tmux
python main.py

Press CTRL + B then D to detach from the session and leave it running in the background. Use tmux attach to reattach.

🤝 Contributors

Utkarsh - Main Developer


🔖 License

This project is licensed under the MIT License - see the LICENSE file for details.

📜 Copyright

© 2024 Alpha Userbot. All rights reserved.

💬 Thanks

We would like to thank the open-source community and contributors for their valuable work.
