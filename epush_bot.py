import telebot

from config import TOKEN_TEST as TOKEN
from database import db
import datetime

bot = telebot.TeleBot(TOKEN, threaded=True)

markup =  telebot.types.InlineKeyboardMarkup()
engagement_button = telebot.types.InlineKeyboardButton(text="Engagement", callback_data="engagement")
warn_button = telebot.types.InlineKeyboardButton(text="Warn", callback_data="warn")
markup.add(engagement_button, warn_button)

register_markup = telebot.types.InlineKeyboardMarkup()
register_button = telebot.types.InlineKeyboardButton(text="Register with Us", callback_data="register_member")
register_markup.add(register_button)

input_markup = telebot.types.InlineKeyboardMarkup()
input_button = telebot.types.InlineKeyboardButton("Username", callback_data="input_user")
input_markup.add(input_button)

force_reply = telebot.types.ForceReply()

dashboard_markup = telebot.types.InlineKeyboardMarkup()
dashboard_button = telebot.types.InlineKeyboardButton(text="Go to Dashboard", callback_data="dashboard")
dashboard_markup.add(dashboard_button)



#################################################################### START HERE #######################
@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.first_name
  
    start_text = f"""
Hello {name}, My name is <b>Deja</b>
I am your personal assistant, I  will 
help you grow your Instagram account with real engagement

But first you need to register to become a member 
Press the register button below
and set your instagram account username e.g @reechee
    """
    bot.send_message(chat_id, text=start_text, reply_markup=register_markup, parse_mode="html")



def input_user_account(message):
    chat_id = message.chat.id
    IG_username = message.text
    name = message.from_user.first_name
    user_id = message.from_user.id
    epush_user = db.Users(
        user_id=user_id,
        name=name,
        username=IG_username,
        join_date=datetime.datetime.now()
    )
    epush_user.commit()
    text = f"""
Congratulations !! You're now a member of epush engagement pool
Your Instagram username is set to <b>@{IG_username}</b>
    """
    bot.send_message(
        chat_id,
        text=text,
        parse_mode="html",
        reply_markup=dashboard_markup
        )


@bot.callback_query_handler(func=lambda call: call.data=="register_member")
def callback_hand(call):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    callback_query_id=call.id
    name = call.from_user.first_name
    message_id = call.message.json['message_id']
    epush_user = db.Users.get(user_id)
    epush_user.delete()
    epush_user=None
    if epush_user:
        username = epush_user.username
        text = f"""
Ooops <b>{name}</b> you are already registered with us.
Your instagram username is set to <b>@{username}</b>.

To change your registered username goto to menu>settings.
You can also contact support to resolve any problem /support.
        """
        bot.send_message(chat_id, text=text, reply_markup=dashboard_markup, parse_mode="html")
    else:
        bot.send_message(
            chat_id, 
            text="Enter your instagram username/handle e.g @reechee",
            reply_markup=force_reply
            )
        bot.register_for_reply_by_message_id(message_id+1, input_user_account)

#         text = """
# Congratulations !!
# You're now a member of epush engagement pool
# Details of the rounds yadayada
# Goto your dashboard to view details and information on the rounds and stats
#         """
#         epush_user = db.Users.create(user_id, name)
#         epush_user.commit()
#         bot.send_message(chat_id, text=text, reply_markup=register_markup)




  

    # bot.answer_callback_query(callback_query_id=callback_query_id, text="Thanks for registering")





# bot.remove_webhook()
bot.polling()