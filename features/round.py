
from config import *

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



def update_round(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    roundlast = db.Rounds.get_lastRound()
    round_id = roundlast.id
    message_id = message.message_id + 1
    drop_duration = roundlast.drop_duration()
    # drop_duration = False

    while drop_duration:
        text=f"""
Engagement push round starts in <b>{drop_duration} seconds</b>
If you wish to join the next round 
Select your username to to join round before round starts
"""
        btn_text=f"@{epush_user.username  {drop_duration}}"
        usern_mrkp = telebot.types.InlineKeyboardMarkup()
        usern_btn = telebot.types.InlineKeyboardButton(text=btn_text, callback_data="join_round")
        usern_mrkp.add(usern_btn)
        bot.edit_message_text(
            text,
            chat_id=user_id,
            message_id=message_id,
            parse_mode="html",
            reply_markup=usern_mrkp
        )
        time.sleep(2)
        drop_duration = roundlast.drop_duration()
        


#     if drop_duration:
#         text=f"""
# Engagement push round starts in <b>{drop_duration} seconds</b>
# If you wish to join the next round 
# Click you username to to join round before round starts
#         """
#         btn_text=f"Join round as: @{epush_user.username}"
#         usern_mrkp = telebot.types.InlineKeyboardMarkup()
#         usern_btn = telebot.types.InlineKeyboardButton(text=btn_text, callback_data="join_round")
#         usern_mrkp.add(usern_btn)
#         bot.edit_message_text(
#             text,
#             chat_id=user_id,
#             message_id=message_id,
#             parse_mode="html",
#             reply_markup=usern_mrkp,
#         )
#     else:

        # import threading
        # def get_thread(thread_name):
        #     for i in threading.enumerate():
        #         if i.name == thread_name:
        #             return i

        # dat_thread = get_thread("update_round_thread")
        # dat_thread.join()
    text = f"""
Round Started 
    """
    bot.edit_message_text(
        text,
        chat_id=user_id,
        message_id=message_id,
        parse_mode="html"
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
.......
{member_list_string}

        """
        bot.edit_message_text(
            text,
            chat_id=user_id,
            message_id=message_id,
            parse_mode="html"
        )
        bot.send_message(
            chat_id=user_id,
            text=list_text,
            parse_mode="html"
        )
    else:
        text = f"""
You missed this round try again next time
    """
        bot.edit_message_text(
            text,
            chat_id=user_id,
            message_id=message_id,
            parse_mode="html"
        )

# def update_thread(message):
#     update_round_thread = RepeatedTimer(5,  update_round,"update_round_thread")
#     try:
#         update_round(message)
#     finally:
#         update_round_thread.stop()



@bot.message_handler(commands=["round"])
def round(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    round_start = db.Rounds.create_now()
    
    drop_duration = round_start.drop_duration()
    def hello(name):
        print ("Hello %s!" % name)

    print("starting...")

    ##this creates a new thread

    text=f"""
Engagement push round starts in <b>{drop_duration} seconds</b>
If you wish to join the next round 
Click you username to to join round before round starts
    """
    # rt = RepeatedTimer(5, hello, "World")
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
    # update_thread(message)
    time.sleep(3)
    # update_round_thread = RepeatedTimer(5,  update_round,"update_round_thread", message)
    round_thread = threading.Timer(1,update_round,args=[message])
    round_thread.name= "round_thread"
    round_thread.start()
    






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


