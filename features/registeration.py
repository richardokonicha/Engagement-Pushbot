

######## REGISTER
from config import *

@bot.callback_query_handler(func=lambda call: call.data=="register_member")
def callback_hand(call):
    bot.answer_callback_query(call.id)
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
Ups 🤷‍♀️ du hast dich schon registriert, <b>{name}</b>.
Dein Instagram Account ist mit  <b>@{username}</b> registriert 
Wenn du deinen Usernamen ändern willst, click einfach auf den Button hier unten 🖱
Du kannst uns auch mit /support kontaktieren
        """
        # bot.send_message(
        #     chat_id, 
        #     text=text, 
        #     reply_markup=dashboard_markup, 
        #     parse_mode="html"
        #     )

        bot.edit_message_text(
            text=text,
            chat_id=user_id,
            message_id=message_id,
            parse_mode="html",
            reply_markup=dashview_markup

            # reply_markup=dashview_markup
        )
    else:
        bot.send_message(
            chat_id, 
            text="Gib bitte deinen Instagram-Nutzernamen mit einem @ davor ein (z.B. „@user123“) 👩🏽🖥️",
            reply_markup=force_reply
            )
        bot.register_for_reply_by_message_id(message_id+1, input_user_account)

####### _change user
@bot.callback_query_handler(func=lambda call: call.data=="input_user")
def input_user(call):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    message_id = call.message.json['message_id']
    epush_user = db.Users.get(user_id)
    bot.send_message(
        user_id, 
        text="Enter your instagram username/handle e.g @reechee",
        reply_markup=force_reply
        )
    bot.register_for_reply_by_message_id(message_id+1, input_user_account)

    
def input_user_account(message):
    chat_id = message.chat.id
    IG_username = message.text
    name = message.from_user.first_name
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    if epush_user == None:
        username=IG_username.strip("@")
        epush_user = db.Users(
            user_id=user_id,
            name=name,
            username=username,
            join_date=datetime.datetime.now()
        )
        epush_user.commit()
        text = f"""
Perfekt! 🥰 Willkommen in der Family. 👨👩👧👦 Dein Instagram-Nutzername ist mit <b>@{IG_username}</b> gespeichert 💾. Du kannst ihn später wieder ändern, falls du das benötigst.
    """
        bot.send_message(
                chat_id,
                text=text,
                parse_mode="html",
                reply_markup=dashboard_markup
                )
                
    else:
        username=IG_username.strip("@")
        epush_user.username=username
        epush_user.commit()
        text = f"""
Your Instagram Username has been changed to {username}
        """
        bot.send_message(
            chat_id,
            text=text,
            parse_mode="html",
            reply_markup=dashboard_markup
            )


