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


@bot.message_handler(regexp='warn')
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
                    text=f"""
<b>🔻WARNUNG {warn_user.warns}/3🔻</b>
Leider hast du die letzte Runde nicht regelkonform abgeschlossen
"""
                    if warn_user.warn>=3:
                        text=f"""
<b>🔻WARNUNG {warn_user.warns}/3🔻</b>
Leider hast du die letzte Runde nicht regelkonform abgeschlossen. Du wurdest nun vom Engagement ausgeschlossen. Bitte kontaktiere den Support 🆘
"""
                    bot.send_message(
                        warn_user.user_id,
                        text=text,
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

        
@bot.message_handler(regexp="free")
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
                    bot.send_message(
                        warn_user.user_id,
                        text=f"""

❇️Freigeschaltet <b>{warn_user.warns}/3</b>❇️
Du wurdest nun wieder freigeschaltet. Viel Spaß!
""",
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



@bot.message_handler(regexp="delete")
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