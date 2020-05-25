############################################################## CALL BACKS  ######################################33
from config import *


######## warns
@bot.callback_query_handler(func=lambda call: call.data=="warns")
def warns(call):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    message_id = call.message.json['message_id']
    epush_user = db.Users.get(user_id)
    warns = epush_user.warns
    lang = epush_user.lang
    text = {
        "en":
        f"""
A warn is a count of the number of times
you have defaulted.
You can default by joining a round and failing to like the last post of
every member in that round. 
Warn count: <b>{warns}</b>
        """,
        "de":
        f"""
Eine Warnung zählt, wie oft
Sie haben standardmäßig.
Sie können standardmäßig einer Runde beitreten und den letzten Beitrag von nicht mögen
jedes Mitglied in dieser Runde.
Anzahl der Warnungen: <b> {warns} </ b>
        """
    }
    bot.edit_message_text(
        text=text,
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html",
        reply_markup=dashview_markup
    )

@bot.callback_query_handler(func=lambda call: call.data=="engagement")
def engagement(call):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    message_id = call.message.json["message_id"]
    epush_user = db.Users.get(user_id)
    engagements = epush_user.pool_count
    lang = epush_user.lang
    next_round = 3
    text = {
        "en":
        f"""
Successful engagement rounds:
<b> {engagements} </b>
The second round started in {next_round} hours

        """,
        "de":
        f"""
Erfolgreiche Engagement-Runden: 
<b>{engagements}</b>
Die nächste Runde startet in {next_round} Stunden
        """
    }
    bot.edit_message_text(
        text=text[lang],
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html",
        reply_markup=dashview_markup
    )

@bot.callback_query_handler(func=lambda call: call.data=="dashboard")
def dashboard(call):
    """dashboard view handler function display next engagement and information"""
    bot.answer_callback_query(call.id, text="dashboard")
    user_id = call.from_user.id
    message_id = call.message.json['message_id'] 
    epush_user = db.Users.get(user_id)
    lang = epush_user.lang
    dashboard_text = {
        "en":
        f"""
<b>Dashboard view</b>
Hello {epush_user.username}
Next engage is 2hours
You would get a reminder 30mins before round starts
        """,
        "de":
        f"""
<b> Dashboard-Ansicht </ b>
Hallo {epush_user.username}
Das nächste Engagement dauert 2 Stunden
Sie würden 30 Minuten vor Beginn der Runde eine Erinnerung erhalten
        """
                }
    bot.edit_message_text(
        text=dashboard_text[lang],
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html",
        reply_markup=dashview_markup
    )

######## _dashboard_
@bot.message_handler(commands=["dashboard", "menu"])
def menu(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    lang = epush_user.lang
    dashboard_text = {
        "en":
        f"""
<b>Dashboard view</b>
Hello {epush_user.username}
Next engage is 2hours
You would get a reminder 30mins before round starts
        """,

        "de":
        f"""
<b> Dashboard-Ansicht </ b>
Hallo {epush_user.username}
Das nächste Engagement dauert 2 Stunden
Sie würden 30 Minuten vor Beginn der Runde eine Erinnerung erhalten
        """
    }
    bot.send_message(
        user_id,
        text=dashboard_text[lang],
        parse_mode="html",
        reply_markup=dashview_markup
    )