

######## REGISTER
from config import *

@bot.callback_query_handler(func=lambda call: call.data=="register_member")
def callback_hand(call):
    """
    this function listens for register member callback button press
    it check it current user is already registered and calls the register_new function
    """
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    name = call.from_user.first_name
    message_id = call.message.json['message_id']
    epush_user = db.Users.get(user_id)
    if epush_user != None:
        username = epush_user.username
        lang = epush_user.lang
        text_register = {
            "en":

            f"""
Oops 🤷‍♀️ you've already registered, <b> {name} </b>.
Your Instagram account is registered with <b> @ {username} </b>
If you want to change your username, just click the button below unten
You can also contact us with / support
            """,

            "de":

            f"""
Ups 🤷‍♀️ du hast dich schon registriert, <b>{name}</b>.
Dein Instagram Account ist mit  <b>@{username}</b> registriert 
Wenn du deinen Usernamen ändern willst, click einfach auf den Button hier unten 🖱
Du kannst uns auch mit /support kontaktieren
            """
        }
        bot.edit_message_text(
            text=text_register[lang],
            chat_id=user_id,
            message_id=message_id,
            parse_mode="html",
            reply_markup=dashview_markup[lang]

            # reply_markup=dashview_markup
        )
    else:
        bot.send_message(
            user_id, 
            text="Please enter your Instagram username with an @ in front (e.g. '@ user123')👩🖥️",
            reply_markup=force_reply
            )
        bot.register_for_reply_by_message_id(message_id+1, register_new_user)

    
def register_new_user(message):
    chat_id = message.chat.id
    insta_username = message.text
    name = message.from_user.first_name
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    if epush_user == None:
        username=insta_username.strip("@")
        epush_user = db.Users(
            user_id=user_id,
            name=name,
            username=username,
            join_date=datetime.datetime.now()
        )
        epush_user.commit()
        text = f"""
Perfect! Welcome to the family. 👨👩👧👦 Your Instagram username is saved with <b> @{username} </b> 💾. You can change it later if you need to.
    """
        bot.send_message(
                chat_id,
                text=text,
                parse_mode="html",
                reply_markup=dashboard_markup["en"]
                )
                
    else:
        username=insta_username.strip("@")
        epush_user.username=username
        epush_user.commit()
        lang = epush_user.lang
        text = {
            "en":
            f"""
Your Instagram Username has been changed to {username}
            """,

            "de":
            f"""
Dein Instagram-Benutzername wurde in {username} geändert.
            """
        }
        bot.send_message(
            chat_id,
            text=text[lang],
            parse_mode="html",
            reply_markup=dashboard_markup[lang]
            )


####### _change user
@bot.callback_query_handler(func=lambda call: call.data=="input_user")
def input_user(call):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    message_id = call.message.json['message_id']
    epush_user = db.Users.get(user_id)
    lang = epush_user.lang
    text = {
        "en": "Enter your instagram username/handle e.g @user123",
        "de": "Geben Sie Ihren Instagram-Benutzernamen / Handle ein, z. B. @ user123"
    }
    bot.send_message(
        user_id, 
        text=text[lang],
        reply_markup=force_reply
        )
    bot.register_for_reply_by_message_id(message_id+1, register_new_user)
