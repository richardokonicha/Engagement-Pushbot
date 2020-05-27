import telebot
import os
from config import *
from flask import Flask, request
server = Flask(__name__)

import importdir
importdir.do("features", globals())

@server.route('/'+ TOKEN, methods=['POST'])
def getMessage():
    request_object = request.stream.read().decode("utf-8")
    update_to_json = [telebot.types.Update.de_json(request_object)]
    bot.process_new_updates(update_to_json)
    return "got Message bro"

@server.route('/hook')
def webhook():
    url=URL
    bot.remove_webhook()
    bot.set_webhook(url + TOKEN)
    return f"Webhook set to {url}"

# @server.route('/round')
# def webhook()


if DEBUG==True:
    bot.remove_webhook()
    bot.polling()
else:
    if __name__ == "__main__":
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

    # bot.polling()
