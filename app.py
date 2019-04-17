# -*- coding: utf-8 -*-
import os
import time

from commands import start_message, new_acknowledgement, button_callback
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#


def error(bot, update, error):
    """Log Errors caused by Updates."""
    print("\n\n****ERROR****\n", error, "\n****ERRND****\n\n")


def main():
    """
        @AcknowledgedBot commands
        /ack - create a new acknowledgement
        /start, /new, /help - Help message
    """

    print("(start) Acknowledged Bot Started")

    # Initialize bot listener
    updater = Updater(token=token)

    # commands
    updater.dispatcher.add_handler(CommandHandler('ack', new_acknowledgement))
    updater.dispatcher.add_handler(CommandHandler('start', start_message))
    updater.dispatcher.add_handler(CommandHandler('new', start_message))
    updater.dispatcher.add_handler(CommandHandler('help', start_message))

    # Button callback
    updater.dispatcher.add_handler(CallbackQueryHandler(button_callback))

    # Errors
    updater.dispatcher.add_error_handler(error)

    # Start listening
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
