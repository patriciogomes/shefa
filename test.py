import telegram

bot = telegram.Bot(token="7752436641:AAH-aJ_B6trDn12a1NjOyh09m6k5JQ1NEiM")
updates = bot.get_updates()
for u in updates:
    print(u.message.chat.id)
