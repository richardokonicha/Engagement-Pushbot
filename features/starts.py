
from config import *


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.first_name
  
    start_text = f"""

Hi {name}, ich bin <b>Claire</b>. 👋🏽🤗

Ich bin deine persönliche Assistentin in Sachen Instagram-Engagement-Growth. 📈😍
Oder mit anderen Worten: ich helfe dir dabei, deine Instagram Reichweite zu erhöhen. 🤓☺️

Zunächst musst du dich hierfür kostenlos registrieren, um teilnehmen zu können.    🙋‍♀️🏽♀

Klick dafür einfach auf den Button hier unten und gib dann deinen Instagram-Nutzernamen ein (z.B. „@user123“) 👩🏽🖥️  

📝Die Regeln lauten wie folgt📝

Jeden Tag finden mehrere Engagement Runden statt 📊. Ich werde dich immer fragen ❓, ob du an der kommenden Runde teilnehmen möchtest. Falls ja, kannst du dich eintragen ✏️ und erhältst bei Start der Runde eine Liste von Accounts in dieser Runde 🧾.

Hier musst du von jedem Account in dieser Runde 
 ⁃ Das Bild liken 💙
 ⁃ Einen Kommentar mit mind. 3 Wörtern/Emojis schreiben 📖

Wenn sich zu viele Personen für eine Runde angemeldet haben, werden die User in Gruppen von maximal 35 Personen geteilt ⚔. Damit sorge ich dafür, dass du nicht 2 Stunden lang nur am Bilder liken und kommentieren bist 😂😘.


Nach 30 Minuten ⏲ wird die Runde beendet. Solltest du nicht alle Accounts geliked/kommentiert haben, bekommst du eine Warnung ⚠️. Bei 5 Warnungen erhältst du einen vorübergehenden Strike ❌.

Viel Spaß und Liebe Grüße,
Claire❤️
    """
    bot.send_message(chat_id, text=start_text, reply_markup=register_markup, parse_mode="html")
