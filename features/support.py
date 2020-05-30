from config import *
from config import ADMIN,bot

def support_response(message, sender_id, message_id):

    response = message.text
    response_text = f"""
<b>📨NEW MAIL FROM SUPPORT </b>/support

<pre>🗣️{response}</pre>"""

    bot.send_message(
        sender_id,
        text=response_text,
        parse_mode="html",
        reply_to_message_id=message_id
    )

    pass

@bot.message_handler(commands=["support"])
def support(message):
    sender_id = message.from_user.id
    message_id = message.message_id
    sender = db.Users.get(sender_id)
    lang = sender.lang
    complaint = message.text.replace("/support", "")
    if complaint:
        refer = f"""

    <b>📨NEW SUPPORT MAIL FROM </b><a href="tg://user?id={sender_id}">@{sender.username}</a>

    <pre>
    🗣️ <i>{complaint}</i>
    </pre>

    <pre><em>Reply this message to respond to @{sender.username}</em></pre>
        """
        for i in ADMIN:    
            outgoing = bot.send_message(
                i,
                text=refer,
                parse_mode="html"
            )
            outgoing_id = outgoing.message_id
            bot.register_for_reply_by_message_id(outgoing_id, support_response, sender_id, message_id)
    else:
        text = {
            "en": """
Improper support request. 
/support has to be followed by your request
<pre>e.g. /support Please reactivate my account</pre>
""",
            "de": """
Unsachgemäße Supportanfrage. 
/support muss von Ihrer Anfrage gefolgt werden
<pre>e.g. /support Bitte reaktiviere mein Konto</pre>

"""
        }
        bot.send_message(
            sender_id,
            text=text[lang],
            parse_mode="html",
            reply_to_message_id=message_id
        )

