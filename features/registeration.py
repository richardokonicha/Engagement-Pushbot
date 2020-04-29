

######## REGISTER
from config import *

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
    warns = epush_user.warns
    text = f"""
A warn is a count of the number of times
you have defaulted.
You can default by joining a round and failing to like the last post of
every member in that round. 
Warn count: <b>{warns}</b>
    """
    bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html",
        reply_markup=dashview_markup

        # reply_markup=dashview_markup
    )

@bot.callback_query_handler(func=lambda call: call.data=="engagement")
def engagement(call):
    user_id = call.from_user.id
    message_id = call.message.json["message_id"]
    epush_user = db.Users.get(user_id)
    engagements = epush_user.pool_count
    text = f"""
Number of successful engagements
<b>{engagements}</b>
Next engagement in 2hours
    """
    bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html",
        reply_markup=dashview_markup
    )


    
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


