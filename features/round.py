
from config import *
import concurrent.futures

def checklist_round(user_id):
    epush_user = db.Users.get(user_id)
    lang = epush_user.lang
    text = {
        "en":
        f"""
The current round ends in 10 minutes.
Please check again if you have an eye on the list
        """,
        "de":
        f"""
In 10 Minuten Endet die aktuelle Runde ⚠️ Bitte check nochmal, ob du die Liste abgearbeitet hast
        """
    }
    bot.send_message(
        chat_id=user_id,
        text=text[lang]
    )

def endof_round(user_id):
    epush_user = db.Users.get(user_id)
    lang = epush_user.lang
    text = {
        "en":
        f"""
The round is over, the next round is at 8:00 p.m.
        """,
        "de":
        f"""
Die Runde ist vorbei, die nächste Runde ist um 20:00 ⏱
        """
    }
    bot.send_message(
        chat_id=user_id,
        text=text[lang]
    )

def start_round(user_id):
    epush_user = db.Users.get(user_id)
    lang = epush_user.lang
    roundlast = db.Rounds.get_lastRound()
    round_id = roundlast.id
    users = db.Users.get_ids()
    drop_duration = roundlast.drop_duration()
    end_round = (roundlast.end()-datetime.datetime.now()).total_seconds()
    text = {
        "en": """The round has started ✅""",
        "de": """Die Runde ist gestartet ✅"""
    }
    bot.send_message(
        chat_id=user_id,
        text=text[lang]
    )
    # gets registered member list and send list to user to like
    def listToString(s):
        str1 = """"""
        for ele in s:
            str1 += (ele+"""
""")
        return str1

    round_current = db.Rounds.get_round(round_id)
    member_list = [i.user_id for i in round_current.memberlist]
    member_list_insta = ["https://www.instagram.com/"+i.username for i in round_current.memberlist]
    member_list_string = listToString(member_list_insta)

    if epush_user.user_id in member_list:
# sends list of registered members to all registered memebers
        list_text = {
            "en":
            f"""
The round has started - here is the list. Please like the latest post from all accounts and leave a compliment comment❤️

{member_list_string}

            """,
            "de":
            f"""
Die Runde ist gestartet - hier ist die Liste. Bitte von allen Accounts den neuesten Post liken und einen regelkonformen Kommentar hinterlassen❤️

{member_list_string}

            """
        }
        bot.send_message(
            chat_id=user_id,
            text=list_text[lang],
            parse_mode="html"
        )
    else:
# Missed the round
        text = {
            "en":
            f"""
Unfortunately you missed the current lap 😫
            """,
            "de":
            f"""
Du hast die aktuelle Runde leider verpasst 😫
            """
        }
        bot.send_message(
            chat_id=user_id,
            text=text[lang],
            parse_mode="html"
        )


@bot.callback_query_handler(func=lambda call: call.data=="join_round")
def join_round(call):   
    user_id = call.from_user.id
    message_id = call.message.message_id
    epush_user = db.Users.get(user_id)
    lang = epush_user.lang
    round_started = db.Rounds.get_lastRound()
    if epush_user.warns>=3:
        text = {
            "en":
            f"""
Sorry you can't join round, you've been blocked
🔴Contact support🔴
            """,
            "de":
            f"""
Es tut uns leid, dass Sie nicht teilnehmen können. Sie wurden blockiert
🔴Kontaktieren Sie Support🔴
            """
        }
        bot.send_message(
            user_id,
            text=text[lang],
            parse_mode="html"
        )
    else:
        if round_started.drop_duration():
            round_started.join(epush_user)
            time_left = round_started.drop_duration()
            text = {
                "en":
                f"""
You are now registered for the next round
                """,
                "de":
                f"""
Du bist nun für die nächste Runde registriert♻️
                """
            }
            bot.send_message(
                user_id,
                text=text[lang],
                parse_mode="html"
            )
        else:
            text = {
                "en":
                f"""
Oopps drop session for the last round has ended
the next round starts in 1hour, be sure not to miss it
                """,
                "de":
                f"""
Die Oopps-Drop-Session für die letzte Runde ist beendet
Die nächste Runde beginnt in 1 Stunde. Verpassen Sie sie nicht
                """
            }
            bot.send_message(
                user_id,
                text=text[lang],
                parse_mode="html"
            )


# Trigger new round function
def round_func():
    """this function initiates a new round and schedules all timed actions"""
    users = db.Users.get_ids()
    round_start = db.Rounds.create_now()
    drop_duration = round_start.drop_duration()
    check_time = round_start.check_time()
    endtime = round_start.end()
    scheduler = BackgroundScheduler()
    timer = datetime.datetime.now() + datetime.timedelta(seconds=drop_duration)

    @scheduler.scheduled_job("date", id="schedsetter", run_date=timer, args=[users])
    def sched_start_round(users):
        """this function anounces the start of a new round to every user, it does this by spliting into multiple threads"""
        for user_id in users:
            round_thread = threading.Timer(1,start_round,args=[user_id])
            round_thread.name= "round_thread"
            round_thread.start()

# messages every user that round is about to checklist
    @scheduler.scheduled_job("date", id="checklist", run_date=check_time, args=[users])
    def check_time(users):
        """this function warns users for few minutes to end of round and to check list for completeness of action"""
        print("checking time")
        roundlast = db.Rounds.get_lastRound()
        round_id = roundlast.id
        round_current = db.Rounds.get_round(round_id)
        member_list = [i.user_id for i in round_current.memberlist]
        for user_id in member_list:
            round_thread = threading.Timer(1,checklist_round,args=[user_id])
            round_thread.name= "checklist_thread"
            round_thread.start()

    @scheduler.scheduled_job("date", id="endoftime", run_date=endtime, args=[users])
    def endof_time(users):
        """this function schedules the function that annouces the end of a round"""
        print("end of time")
        for user_id in users:
            round_thread = threading.Timer(1,endof_round,args=[user_id])
            round_thread.name= "endof_thread"
            round_thread.start()

    scheduler.start()

# messages every user of the round starting in xminutes
    def start_round_thread(user_id):
        user=db.Users.get(user_id)
        lang = user.lang
        btn_text = {
            "en":f"Round started with @{user.username}",
            "de":f"Runde mit @{user.username} beitreten"
        }
        usern_mrkp = telebot.types.InlineKeyboardMarkup()
        usern_btn = telebot.types.InlineKeyboardButton(text=btn_text[lang], callback_data="join_round")
        usern_mrkp.add(usern_btn)

        text = {
            "en":
            f"""
The next engagement round starts in <b> {drop_duration} seconds </b> ⏳. If
you want to participate, just press the button 💁🏽🏽♀
            """,

            "de":
            f"""
Die nächste Engagement-Runde startet in <b>{drop_duration} seconds</b> ⏳. Wenn
du daran teilnehmen möchtest, drücke einfach auf den Button 💁🏽🏽♀
            """
        }
        bot.send_message(
            user_id,
            text=text[lang],
            reply_markup=usern_mrkp,
            parse_mode="html"
        )
    for user_id in users:
        start_round_thread(user_id)
#### ROUND CALLBACK

@bot.message_handler(commands=["round"])
def triggerround(message):
    """this function is called by the clock schedular on heroku to start a round """
    round_func()
    pass