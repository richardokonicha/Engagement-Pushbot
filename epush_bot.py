import telebot

from config import TOKEN_TEST as TOKEN
from database import db
import datetime

bot = telebot.TeleBot(TOKEN, threaded=True)

############################################################ MARKUPS

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

dashview_markup = telebot.types.InlineKeyboardMarkup()
u_btn = telebot.types.InlineKeyboardButton("Edit Username", callback_data="input_user")
e_btn = telebot.types.InlineKeyboardButton("Engagement", callback_data="engagement")
w_btn = telebot.types.InlineKeyboardButton("Warns", callback_data="warns")
# d_btn = telebot.types.InlineKeyboardButton("<<< Go to Dashboard       Next round in 34sec", callback_data="dashboard")
dashview_markup.add(u_btn)
dashview_markup.add(e_btn, w_btn)
# dashview_markup.add(d_btn)

#############################################################     FUNCT     #######################


def input_user_account(message):
    chat_id = message.chat.id
    IG_username = message.text
    name = message.from_user.first_name
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    if epush_user == None:
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
    else:
        text = f"""
Your Instagram Username has been changed to {IG_username}
        """
        bot.send_message(
            chat_id,
            text=text,
            parse_mode="html",
            reply_markup=dashboard_markup
            )


#################################################################### HANDLERS START HERE #######################


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


@bot.message_handler(commands=["dashboard"])
def dashboard(message):
    user_id = message.from_user.id
    message_id = message.json['message_id']
    epush_user = db.Users.get(user_id)
    dashboard_text = """
This is the Dashboard view
Next engage is 2hours
You would get a reminder 30mins before round starts

    """
    bot.send_message(
        user_id,
        text=dashboard_text,
        reply_markup=dashview_markup
        )
    # bot.edit_message_text(
    #     dashboard_text,
    #     user_id,
    #     message_id=message_id,
    #     reply_markup=dashview_markup
    # )


@bot.message_handler(commands=["round"])
def round(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)


    text="""
Engagement push round starts in 30minutes,
If you wish to join the next round 
Click you username to to join round
    """
    btn_text=f"Join round as: @{epush_user.username}"

    usern_mrkp = telebot.types.InlineKeyboardMarkup()
    usern_btn = telebot.types.InlineKeyboardButton(text=btn_text, callback_data="join_round")
    usern_mrkp.add(usern_btn)
    bot.send_message(
        user_id,
        text=text,
        reply_markup=usern_mrkp,
        parse_mode="html"
    )







############################################################## CALL BACKS  ######################################33


######## REGISTER
@bot.callback_query_handler(func=lambda call: call.data=="register_member")
def callback_hand(call):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    callback_query_id=call.id
    name = call.from_user.first_name
    message_id = call.message.json['message_id']
    epush_user = db.Users.get(user_id)
    # epush_user.delete()
    # epush_user=None
    if epush_user != None:
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

####### _change user
@bot.callback_query_handler(func=lambda call: call.data=="input_user")
def input_user(call):
    user_id = call.from_user.id
    message_id = call.message.json['message_id']
    epush_user = db.Users.get(user_id)
    bot.send_message(
        user_id, 
        text="Enter your instagram username/handle e.g @reechee",
        reply_markup=force_reply
        )
    bot.register_for_reply_by_message_id(message_id+1, input_user_account)

######## warns
@bot.callback_query_handler(func=lambda call: call.data=="warns")
def warns(call):
    user_id = call.from_user.id
    message_id = call.message.json['message_id']
    epush_user = db.Users.get(user_id)
    text = """
A warn is a count of the number of times
you have defaulted.
You can default by joining a round and failing to like the last post of
every member in that round. 
Warn count: <b>2</b>
    """
    bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html"
        # reply_markup=dashview_markup
    )


######## _dashboard_
@bot.callback_query_handler(func=lambda call: call.data=="dashboard")
def dashboard(call):
    user_id = call.from_user.id
    message_id = call.message.json['message_id']
    epush_user = db.Users.get(user_id)
    dashboard_text = """
This is the Dashboard view
Next engage is 2hours
You would get a reminder 30mins before round starts

    """
    bot.send_message(
        user_id,
        text=dashboard_text,
        reply_markup=dashview_markup
        )
    # bot.edit_message_text(
    #     dashboard_text,
    #     user_id,
    #     message_id=message_id,
    #     reply_markup=dashview_markup
    # )



#### ROUND
@bot.callback_query_handler(func=lambda call: call.data=="join_round")
def join_round(message):
    


bot.remove_webhook()
bot.polling()