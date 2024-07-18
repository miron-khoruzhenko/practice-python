import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

#doc: Кнопки которые появляются в чате в виде сообщений

# Вставьте ваш токен здесь
bot = telebot.TeleBot("5835450415:AAG53FqTKV8JX5bIXEsUIh35CBmbRClt9QI")

# Функция для старта бота и отображения кнопок
@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("aaaa", callback_data='aaaa'))
    markup.row_width = 2
    markup.add(InlineKeyboardButton("bb", callback_data='bb'), InlineKeyboardButton("cc", callback_data='cc'))
    markup.row_width = 1
    markup.add(InlineKeyboardButton("dddd", callback_data='dddd'))
    
    bot.send_message(message.chat.id, "Выберите одну из кнопок:", reply_markup=markup)

# Функция для обработки нажатий кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "aaaa":
        bot.send_message(call.message.chat.id, "Вы нажали: aaaa")
    elif call.data == "bb":
        bot.send_message(call.message.chat.id, "Вы нажали: bb")
    elif call.data == "cc":
        bot.send_message(call.message.chat.id, "Вы нажали: cc")
    elif call.data == "dddd":
        bot.send_message(call.message.chat.id, "Вы нажали: dddd")

# Запуск бота
bot.polling()

