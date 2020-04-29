############################################################## CALL BACKS  ######################################33
from config import *


######## _dashboard_
@bot.callback_query_handler(func=lambda call: call.data=="dashboard")
def dashboard(call):
    user_id = call.from_user.id
    message_id = call.message.json['message_id']
    epush_user = db.Users.get(user_id)
    dashboard_text = """
<b>Dashboard view</b>
Next engage is 2hours
You would get a reminder 30mins before round starts

    """
    bot.send_message(
        user_id,
        text=dashboard_text,
        reply_markup=dashview_markup,
        parse_mode="html"
        )
    # bot.edit_message_text(
    #     dashboard_text,
    #     user_id,
    #     message_id=message_id,
    #     reply_markup=dashview_markup
    # )

