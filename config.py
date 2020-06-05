
import telebot
from database import db
import datetime
import threading
import os
import re
from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv
load_dotenv()

ADMIN = []
TOKEN = os.getenv("TOKEN")
admin_env = os.getenv("ADMIN")
URL = os.getenv("URL")
DEBUG = (os.getenv("DEBUG") == 'True')

if admin_env == None:
    print("\u001b[31mCannot read ADMIN IDs from environment variable file. Create ADMIN variable in .env file")
else:
    ADMIN = [int(i) for i in admin_env.split(' ')]
if URL == None:
    print("\u001b[31mCannot read TOKEN from environment variable file. Create URL variable in .env file")
if TOKEN==None:
    print("\u001b[36mCannot read TOKEN from environment variable file. Create TOKEN in .env file")


bot = telebot.TeleBot(TOKEN, threaded=True)

next_engagement_annoucement = "30 minutes"
next_engagement = "2 hours"

# assigns sqlite for local environment when debug is true and assigns remote heroku database when debug is false
if DEBUG == True:
    SQLITE = 'sqlite:///database/database.db'
    engine = create_engine(SQLITE, echo=True, connect_args={'check_same_thread': False})
if DEBUG == False:
    DATABASE_URL = os.getenv("DATABASE_URL")
    if DATABASE_URL==None:
        print("Cannot connect to heroku database check exposed vars of postgres setup")
    engine = create_engine(DATABASE_URL, echo=True)
    


############################################################ MARKUPS

markup =  telebot.types.InlineKeyboardMarkup()
engagement_button = telebot.types.InlineKeyboardButton(text="Engagement", callback_data="engagement")
warn_button = telebot.types.InlineKeyboardButton(text="Warnungen`", callback_data="warn")
markup.add(engagement_button, warn_button)

register_markup = telebot.types.InlineKeyboardMarkup()
register_button = telebot.types.InlineKeyboardButton(text="Jetzt registrieren✅", callback_data="register_member")
register_markup.add(register_button)


input_markup = telebot.types.InlineKeyboardMarkup()
input_button = telebot.types.InlineKeyboardButton("Username", callback_data="input_user")
input_markup.add(input_button)

force_reply = telebot.types.ForceReply()
##
dashboard_markup = telebot.types.InlineKeyboardMarkup()
dashboard_button = telebot.types.InlineKeyboardButton(text="Dashboard", callback_data="dashboard")
dashboard_markup.add(dashboard_button)

dashboard_markup_en = telebot.types.InlineKeyboardMarkup()
dashboard_button_en = telebot.types.InlineKeyboardButton(text="Dashboard", callback_data="dashboard")
dashboard_markup_en.add(dashboard_button_en)
dashboard_markup = {
    "en": dashboard_markup_en,
    "de": dashboard_markup
}

###
dashview_markup_de = telebot.types.InlineKeyboardMarkup()
u_btn = telebot.types.InlineKeyboardButton("Nutzername bearbeiten", callback_data="input_user")
e_btn = telebot.types.InlineKeyboardButton("Engagement", callback_data="engagement")
w_btn = telebot.types.InlineKeyboardButton("Warnungen", callback_data="warns")
dashview_markup_de.add(u_btn)
dashview_markup_de.add(e_btn, w_btn)

dashview_markup_en = telebot.types.InlineKeyboardMarkup()
u_btn_en = telebot.types.InlineKeyboardButton("Modify Username", callback_data="input_user")
e_btn_en = telebot.types.InlineKeyboardButton("Engagement", callback_data="engagement")
w_btn_en = telebot.types.InlineKeyboardButton("Warns", callback_data="warns")
dashview_markup_en.add(u_btn_en)
dashview_markup_en.add(e_btn_en, w_btn_en)
dashview_markup = {
    "en": dashview_markup_en,
    "de": dashview_markup_de
}

#############################################################     FUNCT     #######################