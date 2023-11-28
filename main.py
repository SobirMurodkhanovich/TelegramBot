from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Data.config import BOT_TOKEN
from Handlers.users.start import start_handler
from Handlers.users.echo import echo_handler

def main():
    updater = Updater(token=BOT_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, echo_handler ))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
