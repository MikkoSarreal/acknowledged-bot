# -*- coding: utf-8 -*-
import os, time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler



# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
#             ...

def start(bot, update):
    update.message.reply_text("Hello! I'm AcknowledgedBot.\n\nTo make announcements, add me to a group(@AcknowledgedBot) and type \"/ack [your announcement here].\"\n\nIf you find any bugs or suggestions, please message @ackbotsupport.") 


def new(bot, update):
    keyboard = [[InlineKeyboardButton("Acknowledge", callback_data="1")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if ' ' not in update.message.text:
        return
    announcement = update.message.text_markdown.split(" ", 1)[1]
    update.message.reply_text("\n" + announcement  + '\n\n---------------\nAcknowledged:\n', reply_markup=reply_markup, parse_mode= ParseMode.MARKDOWN)
    
def button(bot, update):
    query = update.callback_query
    user = query.from_user
    firstname = user['first_name']
    lastname = user['last_name']

    if firstname is None:
        name = lastname
    elif lastname is None:
        name = firstname
    else:
        name= firstname + ' ' + lastname

    new_name = '- ' + name
    

    if new_name in query.message.text or (' ' + new_name) in query.message.text:
        new_text = query.message.text + ' '
    else:
        new_text =  query.message.text + '\n' + new_name
        ackd_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Acknowledge", callback_data="2")]])
        bot.edit_message_text(reply_markup= ackd_markup , chat_id=query.message.chat_id, message_id=query.message.message_id, text = new_text)
 
'''def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    keyboard = [[InlineKeyboardButton("Acknowledge", callback_data="1")]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="New Announcement (type your message then click this)",
            input_message_content=InputTextMessageContent(query)
            )]
    
    update.inline_query.answer(results)
    update.reply_text(update.message['message_id'],"test",reply_markup=reply_markup)'''
    
def error(bot, update, error):
    """Log Errors caused by Updates."""

def main():
    updater = Updater(token=token)

    updater.dispatcher.add_handler(CommandHandler('ack', new))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('new', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
