import telebot
import webbrowser

bot = telebot.TeleBot('5835450415:AAG53FqTKV8JX5bIXEsUIh35CBmbRClt9QI')

# Обработчик события ввода этих команд. После он вызывает прописанную ниже функцию
@bot.message_handler(commands=['start', 'main'])
def main(message:telebot.types.Message):
    bot.send_message(message.chat.id, 'Привет сучка!')
    bot.send_message(message.chat.id, message.chat.id)

@bot.message_handler(commands=['hello'])    
def main(message:telebot.types.Message):  
    bot.send_message(message.chat.id, f'Hello <b>{message.from_user.full_name}</b>',  parse_mode='html',)

@bot.message_handler(commands=['chat_info'])
def main(message:telebot.types.Message):
    bot.send_message(message.chat.id, message)


@bot.message_handler(commands=['site', 'website'])
def main(message:telebot.types.Message):
    webbrowser.open('www.somelink.com')


@bot.message_handler(commands=['help'])
def main(message:telebot.types.Message):
    bot.send_message(message.chat.id, '<b>Help</b> <u>information <i>text</i></u> (HTML parsed)', parse_mode='html')
    bot.send_message(message.chat.id, '/help - help \n/chat_info - chat info')



# Обработчик всех сообщений а не только команд 
@bot.message_handler()
def main(message:telebot.types.Message):
    msg = message.text.lower()
    chatId = message.chat.id

    if 'привет' in msg:
        bot.send_message(chatId, 'И тебе не хворать')
    elif 'ответь' in msg:
        bot.reply_to(message, 'Вот')
    else:
        bot.send_message(chatId, 'ne diyon abla')
    



# Что бы бот работал бесконечно
bot.polling(none_stop=True)
# bot.infinity_polling()