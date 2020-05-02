
from config import *


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.first_name
  
    start_text = f"""

Hi {name}, ich bin <b>Claire</b>. :wave:🏽🤗

Ich bin deine persönliche Assistentin in Sachen Instagram-Engagement-Growth. :chart_with_upwards_trend::heart_eyes:
Oder mit anderen Worten: ich helfe dir dabei, deine Instagram Reichweite zu erhöhen. 🤓:relaxed:

Zunächst musst du dich hierfür kostenlos registrieren, um teilnehmen zu können. :raising_hand:🏽♀

Klick dafür einfach auf den Button hier unten und gib dann deinen Instagram-Nutzernamen ein (z.B. „@user123“) :woman:🏽:computer:

:memo:Die Regeln lauten wie folgt::memo:

Jeden Tag finden mehrere Engagement Runden statt :bar_chart:. Ich werde dich immer fragen :question:, ob du an der kommenden Runde teilnehmen möchtest. Falls ja, kannst du dich eintragen :pencil2: und erhältst bei Start der Runde eine Liste von Accounts in dieser Runde 🧾.

Hier musst du von jedem Account in dieser Runde 
 ⁃ Das Bild liken :blue_heart:
 ⁃ Einen Kommentar mit mind. 3 Wörtern/Emojis schreiben :book:

Wenn sich zu viele Personen für eine Runde angemeldet haben, werden die User in Gruppen von maximal 35 Personen geteilt ⚔. Damit sorge ich dafür, dass du nicht 2 Stunden lang nur am Bilder liken und kommentieren bist :joy::kissing_heart:.


Nach 30 Minuten ⏲ wird die Runde beendet. Solltest du nicht alle Accounts geliked/kommentiert haben, bekommst du eine Warnung :warning:. Bei 5 Warnungen erhältst du einen vorübergehenden Strike :x:.

Viel Spaß und Liebe Grüße,
Claire:heart:
    """
    bot.send_message(chat_id, text=start_text, reply_markup=register_markup, parse_mode="html")
