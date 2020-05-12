############################################################## CALL BACKS  ######################################33
from config import *


######## _dashboard_
@bot.callback_query_handler(func=lambda call: call.data=="dashboard")
def dashboard(call):
    bot.answer_callback_query(call.id, text="dashboard")
    user_id = call.from_user.id
    message_id = call.message.json['message_id'] 
    epush_user = db.Users.get(user_id)
    dashboard_text = """
<b>Dashboard view</b>
Next engage is 2hours
You would get a reminder 30mins before round starts

    """
    # bot.send_message(
    #     user_id,
    #     text=dashboard_text,
    #     reply_markup=dashview_markup,
    #     parse_mode="html"
    #     )
    bot.edit_message_text(
        text=dashboard_text,
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html",
        reply_markup=dashview_markup
    )


######## warns
@bot.callback_query_handler(func=lambda call: call.data=="warns")
def warns(call):
    bot.answer_callback_query(call.id)
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
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    message_id = call.message.json["message_id"]
    epush_user = db.Users.get(user_id)
    engagements = epush_user.pool_count
    next_round = 3
    text = f"""
Erfolgreiche Engagement-Runden: 
<b>{engagements}</b>
Die nächste Runde startet in {next_round} Stunden
    """
    bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html",
        reply_markup=dashview_markup
    )

