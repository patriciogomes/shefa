import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN must be set in environment variables.")

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher
bot = updater.bot

# Armazena IDs de usuários ativos
ACTIVE_USERS = set()

def send_message(message):
    if not ACTIVE_USERS:
        print("No active users to send message to.")
        return
    for chat_id in ACTIVE_USERS:
        try:
            bot.send_message(chat_id=chat_id, text=message)
        except Exception as e:
            print(f"Failed to send message to {chat_id}: {str(e)}")

# --- Bot Commands ---

def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    ACTIVE_USERS.add(chat_id)
    context.bot.send_message(chat_id=chat_id, text="🤖 Shefa Bot is online and ready for you!")

def status(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="📊 Shefa Engine is running smoothly.")

def stop(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="🛑 Stop command received. (Manual override needed)")

def help_command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    help_text = (
        "/start - Start the Shefa bot\n"
        "/status - Show current bot status\n"
        "/stop - Stop the engine\n"
        "/help - Show this command list"
    )
    context.bot.send_message(chat_id=chat_id, text=help_text)

def setup_bot_commands():
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("status", status))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    print("Telegram bot is running...")
    return updater