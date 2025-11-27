import os, asyncio, datetime
from telethon import TelegramClient, events

api_id   = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
src      = os.getenv("SRC")
dst      = os.getenv("DST")

client = TelegramClient("user", api_id, api_id)

@client.on(events.NewMessage(chats=src))
async def mirror(event):
    await client.send_message(dst, event.message)

async def heartbeat():
    while True:
        print(f"[{datetime.datetime.utcnow():%H:%M}] ♥️  bot still alive")
        await asyncio.sleep(300)   # every 5 min

async def main():
    asyncio.create_task(heartbeat())
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())