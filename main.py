import time
from datetime import datetime
import pytz
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid

# Configuration
api_id = 1234567  # Replace with your API ID
api_hash = "your_api_hash_here"  # Replace with your API hash
string_session = "your_string_session_here"  # Replace with your string session

# Initializing bot and start time
bot = Client("AlphaUserbot", api_id=api_id, api_hash=api_hash, session_string=string_session)
start_time = time.time()  # Track bot uptime
is_spamming = False
is_raiding = False

# Timezone for bot uptime display
timezone = pytz.timezone("Asia/Kolkata")

# Abusive Messages List for Raid
abuses = [
    "Madharchod teri maa ki bur me lund",
    "Bhosdike teri maa ka bhosda",
    "Gaand me danda ghus jaa",
    "Behenchod teri maa ka lauda",
    "Chutiye teri behen ki chut me danda",
    "Saale teri maa ki gaand me aag"
]

# Helper function to calculate uptime
def get_uptime():
    current_time = time.time()
    uptime_seconds = current_time - start_time
    uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
    return uptime_str

# Command: Ban by username
@bot.on_message(filters.command("ban", prefixes=".") & filters.me)
async def ban_member(client, message):
    if len(message.command) > 1:
        username = message.command[1]
        try:
            user = await client.get_users(username)
            await client.ban_chat_member(message.chat.id, user.id)
            await message.reply(f"Banned {user.first_name}.")
        except PeerIdInvalid:
            await message.reply("User not found.")
    else:
        await message.reply("Usage: `.ban @username`")

# Command: Unban by username
@bot.on_message(filters.command("unban", prefixes=".") & filters.me)
async def unban_member(client, message):
    if len(message.command) > 1:
        username = message.command[1]
        try:
            user = await client.get_users(username)
            await client.unban_chat_member(message.chat.id, user.id)
            await message.reply(f"Unbanned {user.first_name}.")
        except PeerIdInvalid:
            await message.reply("User not found.")
    else:
        await message.reply("Usage: `.unban @username`")

# Command: Mute by username
@bot.on_message(filters.command("mute", prefixes=".") & filters.me)
async def mute_member(client, message):
    if len(message.command) > 1:
        username = message.command[1]
        try:
            user = await client.get_users(username)
            await client.restrict_chat_member(message.chat.id, user.id, permissions={"can_send_messages": False})
            await message.reply(f"Muted {user.first_name}.")
        except PeerIdInvalid:
            await message.reply("User not found.")
    else:
        await message.reply("Usage: `.mute @username`")

# Command: Unmute by username
@bot.on_message(filters.command("unmute", prefixes=".") & filters.me)
async def unmute_member(client, message):
    if len(message.command) > 1:
        username = message.command[1]
        try:
            user = await client.get_users(username)
            await client.restrict_chat_member(message.chat.id, user.id, permissions={"can_send_messages": True})
            await message.reply(f"Unmuted {user.first_name}.")
        except PeerIdInvalid:
            await message.reply("User not found.")
    else:
        await message.reply("Usage: `.unmute @username`")

# Command: Kick by username
@bot.on_message(filters.command("kick", prefixes=".") & filters.me)
async def kick_member(client, message):
    if len(message.command) > 1:
        username = message.command[1]
        try:
            user = await client.get_users(username)
            await client.kick_chat_member(message.chat.id, user.id)
            await message.reply(f"Kicked {user.first_name}.")
        except PeerIdInvalid:
            await message.reply("User not found.")
    else:
        await message.reply("Usage: `.kick @username`")

# Command: Promote by username
@bot.on_message(filters.command("promote", prefixes=".") & filters.me)
async def promote_member(client, message):
    if len(message.command) > 1:
        username = message.command[1]
        try:
            user = await client.get_users(username)
            await client.promote_chat_member(message.chat.id, user.id, can_manage_chat=True)
            await message.reply(f"Promoted {user.first_name}.")
        except PeerIdInvalid:
            await message.reply("User not found.")
    else:
        await message.reply("Usage: `.promote @username`")

# Command: Demote by username
@bot.on_message(filters.command("demote", prefixes=".") & filters.me)
async def demote_member(client, message):
    if len(message.command) > 1:
        username = message.command[1]
        try:
            user = await client.get_users(username)
            await client.promote_chat_member(message.chat.id, user.id, can_manage_chat=False)
            await message.reply(f"Demoted {user.first_name}.")
        except PeerIdInvalid:
            await message.reply("User not found.")
    else:
        await message.reply("Usage: `.demote @username`")

# Command: Spam message a number of times
@bot.on_message(filters.command("spam", prefixes=".") & filters.me)
async def spam_message(client, message):
    global is_spamming
    if is_spamming:
        await message.reply("Spam is already in progress. Use `.sspam` to stop.")
        return
    
    if len(message.command) > 2:
        count = int(message.command[1])
        spam_message = " ".join(message.command[2:])
        is_spamming = True
        for _ in range(count):
            if not is_spamming:
                break
            await message.reply(spam_message)
            time.sleep(0.5)
    else:
        await message.reply("Usage: `.spam <count> <message>`")

# Command: Stop spam
@bot.on_message(filters.command("sspam", prefixes=".") & filters.me)
async def stop_spam(client, message):
    global is_spamming
    is_spamming = False
    await message.reply("Stopped spamming.")

# Command: Raid on a specific user
@bot.on_message(filters.command("raid", prefixes=".") & filters.me)
async def raid_command(client, message):
    global is_raiding
    if len(message.command) < 3:
        await message.reply("Usage: `.raid @username <number_of_times>`")
        return

    username = message.command[1]
    raid_count = int(message.command[2])

    try:
        user = await client.get_users(username)
        is_raiding = True
        for _ in range(raid_count):
            if not is_raiding:
                break
            abuse = abuses[_ % len(abuses)]
            await message.reply(f"{user.mention}, {abuse}")
            time.sleep(0.5)
    except PeerIdInvalid:
        await message.reply("User not found.")

# Command: Stop raid
@bot.on_message(filters.command("draid", prefixes=".") & filters.me)
async def stop_raid(client, message):
    global is_raiding
    is_raiding = False
    await message.reply("Raid stopped.")

# Start the bot
if __name__ == "__main__":
    bot.run()
