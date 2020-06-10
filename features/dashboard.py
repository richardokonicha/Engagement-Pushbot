############################################################## CALL BACKS  ######################################33
# from config import *
from config import (
    bot, 
    next_engagement_annoucement, 
    next_engagement, 
    dashboard_markup, 
    dashview_markup, 
    db,
    nextround_timer,
    engagement_time
    )


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
⭕Here you can see the warnings you already have
collected. The warnings are for every round that are not
was completed by the admins. You
You can also contact support at any time if you have any questions.
Simply use "/support followed by the question"

Warn count: <b>{warns}</b>
        """,
        "de":
        f"""
⭕Hier kannst du die Verwarnungen sehen, die du bereits 
gesammelt hast. Die Warnungen werden für jede Runde, die nicht 
vollständig abgeschlossen wurde, von den Admins verteilt. Du
kannst auch jederzeit den Support bei Fragen kontaktieren. 
Hierzu einfach "/support DEINE_FRAGE" nutzen

Anzahl deiner Warnungen: <b>{warns}</b>
        """
    }
    bot.edit_message_text(
        text=text[lang],
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html",
        reply_markup=dashview_markup[lang]
    )

@bot.callback_query_handler(func=lambda call: call.data=="engagement")
def engagement(call):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    message_id = call.message.json["message_id"]
    epush_user = db.Users.get(user_id)
    engagements = epush_user.pool_count
    lang = epush_user.lang

    nextround = nextround_timer(engagement_time)
    next_engagement = f"{nextround['clock']} {nextround['in']}"

    text = {
        "en":
        f"""
Successful engagement rounds: <b> {engagements} </b>
The Next Round would be starting in {next_engagement} hours

        """,
        "de":
        f"""
Erfolgreiche Engagement-Runden: <b>{engagements}</b>
Die nächste Runde startet in {next_engagement} Stunden
        """
    }
    bot.edit_message_text(
        text=text[lang],
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html",
        reply_markup=dashview_markup[lang]
    )

@bot.callback_query_handler(func=lambda call: call.data=="dashboard")
def dashboard(call):
    """dashboard view handler function display next engagement and information"""

    bot.answer_callback_query(call.id, text="dashboard")
    user_id = call.from_user.id
    message_id = call.message.json['message_id'] 
    epush_user = db.Users.get(user_id)
    lang = epush_user.lang
    
    
    nextround = nextround_timer(engagement_time)
    next_engagement = f"{nextround['clock']} {nextround['in']}"
    dashboard_text = {
        "en":
        f"""
<b>Dashboard view</b>
Hello {epush_user.username}
Next engagement is in {next_engagement}
You would get a reminder {next_engagement_annoucement} before round starts
        """,
        "de":
        f"""
<b>Dashboard-Ansicht </b>
Hallo {epush_user.username}
Die nächste Runde startet in {next_engagement}
Du bekommst etwa {next_engagement_annoucement} vor Start der Runde einen Reminder
        """
                }
    bot.send_message(
        chat_id=user_id,
        text=dashboard_text[lang],
        parse_mode="html",
        reply_markup=dashview_markup[lang]
    )

######## _dashboard_
@bot.message_handler(commands=["dashboard", "menu"])
def menu(message):

    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    lang = epush_user.lang

    
    nextround = nextround_timer(engagement_time)
    next_engagement = f"{nextround['clock']} {nextround['in']}"
    dashboard_text = {
        "en":
        f"""
<b>Dashboard view</b>
Hello {epush_user.username}
Next engage is {next_engagement}
You would get a reminder {next_engagement_annoucement} before round starts
        """,

        "de":
        f"""
<b> Dashboard-Ansicht </b>
Hallo {epush_user.username}
Die nächste Runde startet in {next_engagement}
Du bekommst etwa {next_engagement_annoucement} vor Start der Runde einen Reminder
        """
    }

    bot.send_message(
        user_id,
        text=dashboard_text[lang],
        parse_mode="html",
        reply_markup=dashview_markup[lang]
    )