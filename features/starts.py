
from config import *
import time

@bot.message_handler(commands=["start", "Start"])
def start(message):
    user_id = message.from_user.id
    name = message.from_user.first_name

    intro = f"""
Hi {name}, I'm <b> Chuwkudi </b>. 

I'm your personal Instagram engagement growth assistant.
I will help you to increase your Instagram reach. 

First you have to register for free to be able to participate .

Simply click on the button below and then enter your Instagram username (e.g. "@ user123") 

    
    """

    rules = f"""<pre>
"The rules are as follows"

There are several engagement rounds every day 📊. I will always ask you ❓ if you want to participate in the upcoming round. If so, you can register ✏️ and receive a list of accounts in this round at the start of the round   .

Here you have to go from every account in this round
⁃ Like the picture 💙
⁃ Write a comment with at least 3 words / emojis 📖

If too many people have registered for a round, the users are divided into groups of a maximum of 35 people ⚔. This way I make sure that you don't just like and comment on the pictures for 2 hours 😂😘.


The round ends after 30 minutes ⏲. If you have not liked / commented on all accounts, you will receive a warning ⚠️. If you get 5 warnings, you get a temporary strike ❌.

Have fun and greetings,
</pre>
    """

    start_text = {
        "en": f"""
Hi {name}, I'm <b> Chuwkudi </b>. 

I'm your personal Instagram engagement growth assistant.
I will help you to increase your Instagram reach. 🤓☺

First you have to register for free to be able to participate ☺️.

Simply click on the button below and then enter your Instagram username (e.g. "@ user123") 👩🏽🖥️

"The rules are as follows"

There are several engagement rounds every day 📊. I will always ask you ❓ if you want to participate in the upcoming round. If so, you can register ✏️ and receive a list of accounts in this round at the start of the round   .

Here you have to go from every account in this round
⁃ Like the picture 💙
⁃ Write a comment with at least 3 words / emojis 📖

If too many people have registered for a round, the users are divided into groups of a maximum of 35 people ⚔. This way I make sure that you don't just like and comment on the pictures for 2 hours 😂😘.


The round ends after 30 minutes ⏲. If you have not liked / commented on all accounts, you will receive a warning ⚠️. If you get 5 warnings, you get a temporary strike ❌.

Have fun and greetings,

Chukwudi ❤️
    """,

    "de": f"""
Hi {name}, ich bin <b>Chukwudi</b>. 👋🏽🤗

Ich bin deine persönliche Assistentin in Sachen Instagram-Engagement-Growth. 📈😍
Oder mit anderen Worten: ich helfe dir dabei, deine Instagram Reichweite zu erhöhen. 🤓☺️

Zunächst musst du dich hierfür kostenlos registrieren, um teilnehmen zu können ☺️.

Klick dafür einfach auf den Button hier unten und gib dann deinen Instagram-Nutzernamen ein (z.B. „@user123“) 👩🏽🖥️  

📝Die Regeln lauten wie folgt📝

Jeden Tag finden mehrere Engagement Runden statt 📊. Ich werde dich immer fragen ❓, ob du an der kommenden Runde teilnehmen möchtest. Falls ja, kannst du dich eintragen ✏️ und erhältst bei Start der Runde eine Liste von Accounts in dieser Runde 🧾.

Hier musst du von jedem Account in dieser Runde 
⁃ Das Bild liken 💙
⁃ Einen Kommentar mit mind. 3 Wörtern/Emojis schreiben 📖

Wenn sich zu viele Personen für eine Runde angemeldet haben, werden die User in Gruppen von maximal 35 Personen geteilt ⚔. Damit sorge ich dafür, dass du nicht 2 Stunden lang nur am Bilder liken und kommentieren bist 😂😘.


Nach 30 Minuten ⏲ wird die Runde beendet. Solltest du nicht alle Accounts geliked/kommentiert haben, bekommst du eine Warnung ⚠️. Bei 5 Warnungen erhältst du einen vorübergehenden Strike ❌.

Viel Spaß und Liebe Grüße,
Chukwudi❤️
    """,

    }


    bot.send_photo(
        user_id, 
        "https://res.cloudinary.com/konichar/image/upload/v1591791368/bxyknpdz2wuw8ewqevpg.png",
        caption=intro,
        parse_mode="html"
        )
    time.sleep(2)
    bot.send_message(
        user_id,
        text=rules,
        reply_markup=register_markup,
        parse_mode="html"
        )


@bot.message_handler(commands=['lang', 'Lang', "LANG"])
def lang(message):
    user_id = message.from_user.id
    epush_user = db.Users.get(user_id)
    text = message.text
    if re.search('en', text):
        epush_user.lang = "en"
    if re.search('de', text):
        epush_user.lang = "de"
    epush_user.commit()
    lang = epush_user.lang
    text = {
        "en": "Language changed",
        "de": "Sprache geändert"
    }
    bot.send_message(
        user_id,
        text=text[lang],
        parse_mode="html"
        )
