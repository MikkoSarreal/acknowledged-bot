from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode


def start_message(bot, update):
    """Initial start/help message when calling /help or /start"""
    update.message.reply_text(
        "Hello! I'm AcknowledgedBot.\n\nTo make announcements, add me to a group(@AcknowledgedBot) and type \"/ack [your announcement here].\"\n\nIf you find any bugs or suggestions, please message @ackbotsupport.")


def new_acknowledgement(bot, update):
    """Create acknowledgement message for bot"""
    print("(new)", update.effective_user.full_name, update.effective_user.id)

    # Add a "Acknowledge" button, add to reply markup
    keyboard = [[InlineKeyboardButton("Acknowledge", callback_data="1")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # If there is no space, return
    if ' ' not in update.message.text:
        return

    # Split the input message by first space
    announcement = update.message.text_markdown.split(" ", 1)[1]
    final_response = "\n" + announcement + "\n\n---------------\nAcknowledged:\n"

    # Send final message reply
    update.message.reply_text(final_response,
                              reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)


def button_callback(bot, update):
    """Called when user presses Acknowledge Button"""
    print("(ack)", update.effective_user.full_name, update.effective_user.id)
    # Callback query containing all meta data
    query = update.callback_query
    from_user = query.from_user

    # New name
    if from_user.username:
        new_name = '- ' + query.from_user.full_name + \
            ' (@' + from_user.username + ')'
    else:
        new_name = '- ' + query.from_user.full_name

    # Check if already acknowledged
    if new_name in query.message.text or (' ' + new_name) in query.message.text:
        new_text = query.message.text + ' '
        return
    # Add acknowledgement
    else:
        new_text = query.message.text + '\n' + new_name

        # Add Ack button
        ackd_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Acknowledge", callback_data="2")]])
        # Update the message contents
        bot.edit_message_text(reply_markup=ackd_markup, chat_id=query.message.chat_id,
                              message_id=query.message.message_id, text=new_text)
    query.answer()
