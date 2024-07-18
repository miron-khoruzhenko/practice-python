import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# doc: 2024.07.12 - Part 2 кнопки которые появляются в чате в меню а так же второй уровень меню

# Вставьте ваш токен здесь
bot = telebot.TeleBot("5835450415:AAG53FqTKV8JX5bIXEsUIh35CBmbRClt9QI")

# Функция для старта бота и отображения кнопок
@bot.message_handler(commands=['start'])
def start(message):
    main_menu(message.chat.id)

# Функция для отображения главного меню
def main_menu(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.row_width = 1
    markup.add(KeyboardButton("aaaa"))
    markup.row_width = 2
    markup.add(KeyboardButton("bb"), KeyboardButton("cc"))
    markup.row_width = 1
    markup.add(KeyboardButton("dddd"))
    bot.send_message(chat_id, "Выберите одну из кнопок:", reply_markup=markup)

# Функция для отображения второго уровня меню
def submenu_aaaa(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.row_width = 2
    markup.add(KeyboardButton("eeee"), KeyboardButton("ffff"))
    markup.row_width = 1
    markup.add(KeyboardButton("Назад"))
    bot.send_message(chat_id, "Вы выбрали aaaa. Выберите одну из кнопок:", reply_markup=markup)

# Функция для обработки нажатий кнопок
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    
    if message.text == "aaaa":
        submenu_aaaa(chat_id)
    elif message.text == "bb":
        bot.send_message(chat_id, "Вы нажали: bb")
    elif message.text == "cc":
        bot.send_message(chat_id, "Вы нажали: cc")
    elif message.text == "dddd":
        bot.send_message(chat_id, "Вы нажали: dddd")
    elif message.text == "eeee":
        bot.send_message(chat_id, "Вы нажали: eeee")
    elif message.text == "ffff":
        bot.send_message(chat_id, "Вы нажали: ffff")
    elif message.text == "Назад":
        main_menu(chat_id)
    else:
        bot.send_message(chat_id, "Пожалуйста, выберите одну из кнопок.")

# Запуск бота
bot.polling()
