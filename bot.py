import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def new_message_handler(event):
    print(f"New Message: {event.message.text}")

async def main():
    print(f"Listening for new messages in {CHANNEL_USERNAME}...")
    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())
