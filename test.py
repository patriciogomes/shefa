import asyncio
from telegram import Bot

async def get_chat_id():
    bot = Bot(token="7752436641:AAH-aJ_B6trDn12a1NjOyh09m6k5JQ1NEiM")
    updates = await bot.get_updates()
    for u in updates:
        print("Chat ID:", u.message.chat.id)

asyncio.run(get_chat_id())


