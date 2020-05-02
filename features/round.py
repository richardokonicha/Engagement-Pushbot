
from config import *
import concurrent.futures

import sched, time
def end_round(user_id):
    text="Round has ended"
    bot.send_message(
        user_id,
        text=text,
        parse_mode="html"
    )
def run_sched(user_id, duration):
    s = sched.scheduler(time.time, time.sleep)
    s.enter(duration, 1, end_round, argument=(user_id,))
    s.run()



def update_round(message, user_id):
    print("MESSAGE________________________+++++++++++++++++++++++++++", message.message_id)
    # user_id = message.from_user.id

    epush_user = db.Users.get(user_id)
    roundlast = db.Rounds.get_lastRound()
    round_id = roundlast.id
    users = db.Users.get_ids()
    message_id = message.message_id + users.index(user_id)
    drop_duration = roundlast.drop_duration()
    end_round = (roundlast.end()-datetime.datetime.now()).total_seconds()
    time.sleep(drop_duration)

    # drop_duration = False
    # while drop_duration:
        
#         text=f"""
# Engagement push round starts in <b>{drop_duration} seconds</b>
# If you wish to join the next round 
# Select your username to to join round before round starts
# """
#         btn_text=f"@{epush_user.username} -----{drop_duration}"
#         usern_mrkp = telebot.types.InlineKeyboardMarkup()
#         usern_btn = telebot.types.InlineKeyboardButton(text=btn_text, callback_data="join_round")
#         usern_mrkp.add(usern_btn)
#         bot.edit_message_text(
#             text,
#             chat_id=user_id,
#             message_id=message_id,
#             parse_mode="html",
#             reply_markup=usern_mrkp
#         )
#         time.sleep(2)
        # drop_duration = roundlast.drop_duration()
        # drop_duration = False


    text = f"""
Round Started 
    """
    bot.send_message(
        # text,
        # chat_id=user_id,
        # message_id=message_id,
        # parse_mode="html"
        
        chat_id=user_id,
        text=text

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
    member_list_insta = ["@"+i.username for i in round_current.memberlist]
    member_list_string = listToString(member_list_insta)

    if epush_user.user_id in member_list:
        text = f"""
Please follow all Engagement instructions

        """
        list_text = f"""
....... LIST OF USERS TO LIKE.........
{member_list_string}

        """
        # bot.edit_message_text(
        #     text,
        #     chat_id=user_id,
        #     message_id=message_id,
        #     parse_mode="html"
        # )
        bot.send_message(
            chat_id=user_id,
            text=list_text,
            parse_mode="html"
        )
        end_round = (roundlast.end()-datetime.datetime.now()).total_seconds()
        time.sleep(end_round)
        text = "Round has ended successfully"
        bot.send_message(
            chat_id=user_id,
            text=text,
            parse_mode="html"
        )
    else:
        text = f"""
You missed this round try again next time
    """
        bot.send_message(
            chat_id=user_id,
            text=text,
            parse_mode="html"
        )

# def update_thread(message):
#     update_round_thread = RepeatedTimer(5,  update_round,"update_round_thread")
#     try:
#         update_round(message)
#     finally:
#         update_round_thread.stop()

@server.route("/round")
@bot.message_handler(commands=["round"])
def round_func(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    users = db.Users.get_ids()
    round_start = db.Rounds.create_now()
    drop_duration = round_start.drop_duration()
    print("starting...")
    ##this creates a new thread
    text=f"""
Die nächste Engagement-Runde startet in <b>{drop_duration} seconds</b> :hourglass_flowing_sand:. Wenn
du daran teilnehmen möchtest, drücke einfach auf den Button :information_desk_person:🏽♀
    """
    # rt = RepeatedTimer(5, hello, "World")
    btn_text=f"Runde mit @{epush_user.username} beitreten."
    usern_mrkp = telebot.types.InlineKeyboardMarkup()
    usern_btn = telebot.types.InlineKeyboardButton(text=btn_text, callback_data="join_round")
    usern_mrkp.add(usern_btn)
    def start_round_thread(user_id):
        bot.send_message(
            user_id,
            text=text,
            reply_markup=usern_mrkp,
            parse_mode="html"
        )
        # update_thread(message)
        time.sleep(1)
        # update_round_thread = RepeatedTimer(5,  update_round,"update_round_thread", message)
        round_thread = threading.Timer(1,update_round,args=[message, user_id])
        round_thread.name= "round_thread"
        round_thread.start()
        
    # with concurrent.futures.ThreadPoolExecutor(max_workers=len(users)) as e:
    #     e.map(start_round_thread, users)
    for user_id in users:
        start_round_thread(user_id)





#### ROUND CALLBACK


@bot.callback_query_handler(func=lambda call: call.data=="join_round")
def join_round(call):   
    user_id = call.from_user.id
    message_id = call.message.message_id
    epush_user = db.Users.get(user_id)
    round_started = db.Rounds.get_lastRound()
    if round_started.drop_duration():
        round_started.join(epush_user)
        time_left = round_started.drop_duration()
        #TODO remove pause here
        # run_sched(user_id, 20)
        text = f"""You've been added to the list of the next round
<b>Stay tuned</b>
"""
        bot.send_message(
            user_id,
            text=text,
            parse_mode="html"
        )
        # bot.edit_message_text(
        #     text,
        #     chat_id=user_id,
        #     message_id=message_id,
        #     parse_mode="html"
        # )
    else:
        text = f"""Oopps drop session for the last round has ended
the next round starts in 1hour, be sure not to miss it"""
        bot.send_message(
            user_id,
            text=text,
            parse_mode="html"
        )


