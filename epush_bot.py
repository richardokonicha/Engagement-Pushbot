import telebot

from config import *


import importdir
importdir.do("features", globals())



# bot.remove_webhook()
bot.polling()