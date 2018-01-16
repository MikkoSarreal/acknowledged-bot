# -*- coding: utf-8 -*-
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#             ...

def new(bot, update):

    
    keyboard = [[InlineKeyboardButton("Acknowledge", callback_data="1")]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("\n" + update.message.text.split(" ", 1)[1] + '\n\nAcknowledged:\n', reply_markup=reply_markup)
    

def button(bot, update):
    query = update.callback_query

    
    new_name = '-'+query.from_user['first_name']+' '+query.from_user['last_name']

    if new_name in query.message.text:
        new_text = query.message.text + ' '
    else:
        new_text =  query.message.text + '\n' + new_name
        ackd_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Acknowledge", callback_data="2")]])
        bot.edit_message_text(reply_markup= ackd_markup , chat_id=query.message.chat_id, message_id=query.message.message_id, text = new_text)

 

    
    
def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)



def main():
    updater = Updater(token=token)

    updater.dispatcher.add_handler(CommandHandler('ack', new))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_error_handler(error)



    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

