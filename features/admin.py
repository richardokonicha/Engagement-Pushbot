from config import *

def listToString(s):
    str1 = """"""
    for ele in s:
        str1 += (ele+"""
""")
    return str1

# prepares warn list for admin
def warn_status(stype=None):
    all_epush_users = db.Users.get_users()
    list_insta = ["@"+i.username+" - "+"⚠️warns "+str(i.warns) for i in all_epush_users]

    if stype=='ids':
        list_insta = ["@"+i.username+" - "+" ID "+str(i.user_id) for i in all_epush_users]
    list_string = listToString(list_insta)
    list_text = f"""
🥬User warn status - use command /warn user to send warn🥬

{list_string}

"""
    return list_text


@bot.message_handler(commands=["warn"])
def admin_view(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    if epush_user.user_id in ADMIN:
        findall = re.findall('@[\w\.]+', message.text)
        if findall:
            for item in findall:
                itemi=item.strip("@")
                warn_user=db.Users.get_username(itemi)
                if warn_user:
                    warn_user.warning()
                    warn_user.commit()
                    lang = warn_user.lang
                    text= {
                        "en":f"""
<b>🔻WARNING {warn_user.warns}/3🔻</b>
Unfortunately, you did not complete the last round in accordance with the rules
""",
                        "de":f"""
<b>🔻WARNUNG {warn_user.warns}/3🔻</b>
Leider hast du die letzte Runde nicht regelkonform abgeschlossen
"""
                    }
                    if warn_user.warns>=3:
                        text= {
                        "en":f"""
<b>🔻WARNING {warn_user.warns}/3🔻</b>
Unfortunately, you did not complete the last round in accordance with the rules. You have now been excluded from engagement. Please contact support 🆘
""",
                        "de":f"""
<b>🔻WARNUNG {warn_user.warns}/3🔻</b>
Leider hast du die letzte Runde nicht regelkonform abgeschlossen. Du wurdest nun vom Engagement ausgeschlossen. Bitte kontaktiere den Support 🆘
"""
                    }
                    bot.send_message(
                        warn_user.user_id,
                        text=text[lang],
                        parse_mode="html"
                    )
                else:
                    text=f"🔴 {item} is not a User - Check name 🔴"
                    bot.send_message(
                        user_id,
                        text=text,
                        parse_mode="html"
                    )
    
        list_text = warn_status()
        bot.send_message(
            user_id,
            text=list_text,
            parse_mode="html"
        )
    else:
        text="You dont have access"
        bot.send_message(
            user_id,
            text=text
        )

        
@bot.message_handler(commands=["free"])
def free(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    if epush_user.user_id in ADMIN:
        findall = re.findall('@[\w\.]+', message.text)
        if findall:
            for item in findall:
                itemi=item.strip("@")
                warn_user=db.Users.get_username(itemi)
                if warn_user:
                    warn_user.warns=0
                    warn_user.commit()
                    lang=warn_user.lang
                    text= {
                        "en":f"""
❇️Unblocked<b>{warn_user.warns}/3</b>❇️
You have now been unlocked again. Have fun!
""",
                        "de":f"""
❇️Freigeschaltet <b>{warn_user.warns}/3</b>❇️
Du wurdest nun wieder freigeschaltet. Viel Spaß!
"""
                    }
                    bot.send_message(
                        warn_user.user_id,
                        text=text[lang],
                        parse_mode="html"
                        )
                else:
                    text=f"🔴 {item} is not a User - Check name 🔴"
                    bot.send_message(
                        user_id,
                        text=text,
                        parse_mode="html"
                    )
    
        list_text = warn_status()
        bot.send_message(
            user_id,
            text=list_text,
            parse_mode="html"
        )
    else:
        text="You dont have access"
        bot.send_message(
            user_id,
            text=text
        )



@bot.message_handler(commands=["delete"])
def delete_user(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    if epush_user.user_id in ADMIN:
        findall = re.findall('@[\w\.]+', message.text)
        if findall:
            for item in findall:
                itemi=item.strip("@")
                del_user=db.Users.get_username(itemi)
                if del_user:
                    lang = del_user.lang
                    del_user.delete()
                    text = {
                        "en": "You have been deleted to register again use command /start",
                        "de": "Sie wurden gelöscht, um sich mit dem Befehl erneut zu registrieren /start"
                    }
                    bot.send_message(
                        del_user.user_id,
                        text=text[lang],
                        parse_mode="html"
                        )
                else:
                    text=f"🔴 {item} is not a User - Check name 🔴"
                    bot.send_message(
                        user_id,
                        text=text,
                        parse_mode="html"
                    )
    
        list_text = warn_status()
        bot.send_message(
            user_id,
            text=list_text,
            parse_mode="html"
        )
    else:
        text="You dont have access"
        bot.send_message(
            user_id,
            text=text
        )


@bot.message_handler(regexp='allusers')
def allusers(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    if epush_user.user_id in ADMIN:
        list_text = warn_status(stype='ids')
        bot.send_message(
            user_id,
            text=list_text,
            parse_mode="html"
        )


@bot.message_handler(regexp='test_round\s\d+')
def test_round(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    lang = epush_user.lang
    round_started = db.Rounds.get_lastRound()
    test_num = int(message.text.split(" ")[-1])
    if round_started.drop_duration():
        for i in range(test_num):
            test_user = db.Users(
                user_id=90909000+i,
                name=f"test_user {i}",
                username=f"test_user{i}",
                join_date=datetime.datetime.now()
            )
            round_started.join(test_user)
        text = {
            "en":
            f"""
    Test user are now registered for the next round
            """,
            "de":
            f"""
    test Du bist nun für die nächste Runde registriert♻️
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

