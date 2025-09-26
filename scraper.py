from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
channel = 'leak_channel_name'

client = TelegramClient('session_name', api_id, api_hash)

async def scrape():
    await client.start()
    history = await client(GetHistoryRequest(
        peer=channel,
        limit=100,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))
    for msg in history.messages:
        print(msg.message)

client.loop.run_until_complete(scrape())
