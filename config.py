
import telebot
from database import db
import datetime
import threading

from apscheduler.schedulers.background import BackgroundScheduler

# bot = telebot.TeleBot(TOKEN, threaded=True)
# TOKEN = "1128492285:AAHzvyFybBx-a7RYZia5hLaXmq1TPpgVd9E"
# TOKEN = "852053528:AAHL_ryUUJ1JOhenzmI0WDiayAnxxqGFmyU"
# URL = 'https://84b2f139.ngrok.io/'
URL = 'https://epush-bot.herokuapp.com/'
bot = telebot.TeleBot(TOKEN, threaded=True)
bot_remind = telebot.TeleBot(TOKEN, threaded=True)

bot.worker_pool

############################################################ MARKUPS

markup =  telebot.types.InlineKeyboardMarkup()
engagement_button = telebot.types.InlineKeyboardButton(text="Engagement", callback_data="engagement")
warn_button = telebot.types.InlineKeyboardButton(text="Warnungen`", callback_data="warn")
markup.add(engagement_button, warn_button)

register_markup = telebot.types.InlineKeyboardMarkup()
register_button = telebot.types.InlineKeyboardButton(text="Register with Us", callback_data="register_member")
register_markup.add(register_button)


input_markup = telebot.types.InlineKeyboardMarkup()
input_button = telebot.types.InlineKeyboardButton("Username", callback_data="input_user")
input_markup.add(input_button)

force_reply = telebot.types.ForceReply()

dashboard_markup = telebot.types.InlineKeyboardMarkup()
dashboard_button = telebot.types.InlineKeyboardButton(text="Dashboard", callback_data="dashboard")
dashboard_markup.add(dashboard_button)

dashview_markup = telebot.types.InlineKeyboardMarkup()
u_btn = telebot.types.InlineKeyboardButton("Nutzername bearbeiten", callback_data="input_user")
e_btn = telebot.types.InlineKeyboardButton("Engagement", callback_data="engagement")
w_btn = telebot.types.InlineKeyboardButton("Warns", callback_data="warns")
# d_btn = telebot.types.InlineKeyboardButton("<<< Go to Dashboard       Next round in 34sec", callback_data="dashboard")
dashview_markup.add(u_btn)
dashview_markup.add(e_btn, w_btn)
# dashview_markup.add(d_btn)

#############################################################     FUNCT     #######################
