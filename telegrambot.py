from transliterate import to_cyrillic, to_latin
import telebot
TOKEN='5466133930:AAFKk-LJAF-dGn7t3RDngVax7qgXrYS7zEA'
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob=("Assalomu alaykum. Xush kelipsiz!")
    javob+="\nMatn kiriting:"
    bot.reply_to(message,javob)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinity_polling()



# matn=input('Matn kiriting: ')
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))