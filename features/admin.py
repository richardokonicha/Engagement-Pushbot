from config import *

@bot.message_handler(regexp='sudo')
def admin_view(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    if epush_user.user_id == ADMIN:
        all_epush_users = db.Users.get_ids()

        key_b=telebot.types.InlineKeyboardButton(text=f"{epush_user.name}", callback_data="toggle")
        key_m=telebot.types.InlineKeyboardMarkup()
        key_m.add(key_b)
        text="List of users"
        bot.send_message(
            user_id,
            text=text,
            reply_markup=key_m,
            parse_mode="html"
        )
    else:
        text="You dont have access"
        bot.send_message(
            user_id,
            text=text
        )