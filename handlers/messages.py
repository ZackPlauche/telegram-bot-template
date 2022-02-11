from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
echo = MessageHandler(Filters.text & (~Filters.command), echo)

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
unknown = MessageHandler(Filters.command, unknown)