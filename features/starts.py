
from config import *


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.first_name
  
    start_text = f"""
Hello {name}, My name is <b>Deja</b>
I am your personal assistant, I  will 
help you grow your Instagram account with real engagement

But first you need to register to become a member 
Press the register button below
and set your instagram account username e.g @reechee
    """
    bot.send_message(chat_id, text=start_text, reply_markup=register_markup, parse_mode="html")
