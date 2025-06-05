import os
import telebot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN must be set in environment variables.")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
ACTIVE_USERS = set()

def send_message(message):
    if not ACTIVE_USERS:
        print("No active users to send message to.")
        return
    for chat_id in ACTIVE_USERS:
        try:
            bot.send_message(chat_id, message)
        except Exception as e:
            print(f"Error sending to {chat_id}: {str(e)}")

@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    ACTIVE_USERS.add(chat_id)
    bot.send_message(chat_id, "🤖 Shefa Bot is online and ready!")

@bot.message_handler(commands=['status'])
def status_handler(message):
    bot.send_message(message.chat.id, "📊 Shefa Engine is running.")

@bot.message_handler(commands=['stop'])
def stop_handler(message):
    bot.send_message(message.chat.id, "🛑 Stop command received (manual override needed).")

@bot.message_handler(commands=['help'])
def help_handler(message):
    help_text = (
        "/start - Start the Shefa bot\n"
        "/status - Show current bot status\n"
        "/stop - Stop the engine\n"
        "/help - Show this command list"
    )
    bot.send_message(message.chat.id, help_text)

def setup_bot_commands():
    print("✅ Telebot bot is polling...")
    bot.polling()