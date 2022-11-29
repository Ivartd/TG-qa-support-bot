import os
from telegram.ext import Updater
import telebot;
from telebot import types;
from telegram import *
from telegram.ext import *
from requests import *
from telegram.ext import CommandHandler, MessageHandler, Filters

telgramSupportChatId = int("CHAT ID")
updater = Updater(token = "BOT TOKEN")
dispatcher = updater.dispatcher

WRONG_REPLY = "WRONG REPLY"
REPLY_TO_THIS_MESSAGE = "CANT REPLY DUE SECURITY, REPLY TO THIS"

firstButton = "BUTTON NAME/QUESTION"
secondButton = "BUTTON NAME/QUESTION"
thirdButton = "BUTTON NAME/QUESTION"
fourthButton = "BUTTON NAME/QUESTION"


def start(update, context):

    buttons = [[KeyboardButton(firstButton)], 
    [KeyboardButton(secondButton)],
    [KeyboardButton(thirdButton)],
    [KeyboardButton(fourthButton)]]
    
    context.bot.send_message(chat_id=update.effective_chat.id,
    text="WELCOMING MESSAGE",
    reply_markup = ReplyKeyboardMarkup(buttons))

    user_info = update.message.from_user.to_dict()
   
def forward_to_chat(update, context):
    forwarded = update.message.forward(chat_id=telgramSupportChatId)

    if sizesButton in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "ANSWER")
    if sewTimeButton in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "ANSWER")
    if giftCardButton in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "ANSWER")
    if supportButton in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text = "ANSWER")
        if not forwarded.forward_from:
            context.bot.send_message(
                chat_id=telgramSupportChatId,
                reply_to_message_id=forwarded.message_id,
                text=f'{update.message.from_user.id}\n{REPLY_TO_THIS_MESSAGE}'
            )
    else:
        if not forwarded.forward_from:
            context.bot.send_message(
                chat_id=telgramSupportChatId,
                reply_to_message_id=forwarded.message_id,
                text=f'{update.message.from_user.id}\n{REPLY_TO_THIS_MESSAGE}'
            )


def forward_to_user(update, context):
    user_id = None
    if update.message.reply_to_message.forward_from:
        user_id = update.message.reply_to_message.forward_from.id
    elif REPLY_TO_THIS_MESSAGE in update.message.reply_to_message.text:
        try:
            user_id = int(update.message.reply_to_message.text.split('\n')[0])
        except ValueError:
            user_id = None
    if user_id:
        context.bot.copy_message(
            message_id=update.message.message_id,
            chat_id=user_id,
            from_chat_id=update.message.chat_id
        )
    else:
        context.bot.send_message(
            chat_id=TELEGRAM_SUPPORT_CHAT_ID,
            text=WRONG_REPLY
        )

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.chat_type.private, forward_to_chat))
dispatcher.add_handler(MessageHandler(Filters.chat(telgramSupportChatId) & Filters.reply, forward_to_user))

updater.start_polling()
updater.idle()
