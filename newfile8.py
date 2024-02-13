import telebot
from datetime import datetime

bot = telebot.TeleBot("6740777226:AAGC-CQdRx4xFx8r3fIM-6f7yfOONMTv0GU")
dev = 6454550864
n = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "هلا حبيبي البوت يحسب الفرق بين تاريخين \n ارسل هسه التاريخ الاول بهشكل \n 2023 1 1 .")
    if message.from_user.id not in n:
        n[message.from_user.id] = message.from_user.first_name
        name = message.from_user.first_name
        id = message.from_user.id
        bot.send_message(dev, f"شخص جديد [{name}](tg://user?id={id}) ، {id}", parse_mode="markdown")
        with open('idididid.txt', 'a') as file:
            file.write(str(message.from_user.id) + '\n')

@bot.message_handler(func=lambda message: len(message.text.split()) == 3)
def _(message):
    try:
        dd = datetime.strptime(message.text, '%Y %m %d')
        bot.reply_to(message, f"حلو التاريخ الاول {message.text} \n ارسل هسه التاريخ الثاني  بنفس الشكل .")
        bot.register_next_step_handler(message, _, dd)
    except ValueError:
        bot.reply_to(message, "حبيبي ارسل تاريخ صحيح بس .")

def _(message, dd):
    try:
        ddd = datetime.strptime(message.text, '%Y %m %d')
        dif = ddd - dd
        day = dif.days
        week = day // 7
        mo = ddd.month - dd.month + 12 * (ddd.year - dd.year)
        yea = ddd.year - dd.year
        bot.reply_to(message, f'''*▫️الفرق بين التاريخين المرسلات .▫️*
مر على هذا التاريخ بـ *الايام ⦗ {day} ⦘* يوم .
مر على هذا التاريخ بـ *الاسابيع ⦗ {week} ⦘* اسبوع .
مر على هذا التاريخ بـ *الاشهر ⦗ {mo} ⦘* شهر .
مر على هذا التاريخ بـ *السنوات ⦗ {yea} ⦘* سنة .''', parse_mode="markdown")
    except ValueError:
        bot.reply_to(message, "حبيبي ارسل تاريخ صحيح بس .")

bot.infinity_polling()