from config import *

def listToString(s):
    str1 = """"""
    for ele in s:
        str1 += (ele+"""
""")
    return str1

# prepares warn list for admin
def warn_status():
    all_epush_users = db.Users.get_users()
    list_insta = ["@"+i.username+" - "+"⚠️warns "+str(i.warns) for i in all_epush_users]
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
    if epush_user.user_id == ADMIN:
        findall = re.findall('@[\w\.]+', message.text)
        if findall:
            for item in findall:
                itemi=item.strip("@")
                warn_user=db.Users.get_username(itemi)
                if warn_user:
                    warn_user.warning()
                    warn_user.commit()
                    bot.send_message(
                        warn_user.user_id,
                        text=f"""
<b>🔻warning🔻{warn_user.warns}</b>
Requirements incomplete  -- You get blocked after 3 warns""",
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
    if epush_user.user_id == ADMIN:
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
<b>🥬Freed🥬{warn_user.warns}</b>
Requirements incomplete  -- You get blocked after 3 warns""",
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
