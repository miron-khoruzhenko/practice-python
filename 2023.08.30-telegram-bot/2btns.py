import telebot
from telebot import types
from telebot.types import Message, CallbackQuery

from datetime import datetime
import os 
import requests

bot_token = '5835450415:AAG53FqTKV8JX5bIXEsUIh35CBmbRClt9QI'
bot = telebot.TeleBot(bot_token)

# @bot.message_handler(commands=['send_elif'])
# def message_with(message : Message):

#   bot.send_message(5612474867, 'Yay we have an upgrade, now you can send your nudes and not be afraid that they will not reach! ?')


def covert_timestamp(hour):
  return datetime.fromtimestamp(hour)


def chat_log(
    msg_obj : Message, 
    bot_reply : str = '', 
    manuel_msg : str = '', 
    isConsolePrinting : bool = True, 
    isSystemMsg : bool = False
  ):
  '''
  Берет объект сообщения (msg_obj) и на основе данных из него
  - Сохраняет если есть сообщение пользователя и бота
  - Сохраняет введенное вручную сообщение(msg_text) и игнорирует сообщение пользователя
  - Сохраняет системные сообщения и игнорирует сообщение бота и пользователя 
  '''

  if not manuel_msg:
    message = msg_obj.text.lower()
  elif manuel_msg:
    message = manuel_msg  
  else:
    print('Something went wrong!')

  user_fullname = msg_obj.from_user.full_name
  username = msg_obj.from_user.username

  chat_id = msg_obj.chat.id
  msg_date = covert_timestamp(msg_obj.date)


  if message != '' or bot_reply != '':
    with open(f'{chat_id}:{username}-{user_fullname}.log', 'a') as file:
      if message != '' and not isSystemMsg:
        file.write(f'{msg_date} - {username}: {message}\n')

        if isConsolePrinting:
          print(f'{user_fullname}: {message}')


      if bot_reply != '' and not isSystemMsg:
        file.write(f'{msg_date} - BOT: {bot_reply}\n')
      
        if isConsolePrinting:
          print(f'{" "*(len(user_fullname) - 3)}bot: {bot_reply}')

      if isSystemMsg:
        file.write(f'{msg_date} - SYSTEM: {manuel_msg}\n')

        if isConsolePrinting:
          print(f'{" "*(len(user_fullname) - len("system"))}SYSTEM: {manuel_msg}')


    
def save_img_and_get_url(message : Message):
  photo = message.photo[-1]  # Get the largest available photo (usually the last one in the list)
  
  # Download the photo by file ID
  file_info = bot.get_file(photo.file_id)
  file_path = file_info.file_path
  file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_path}"
  
  # Choose a local file path to save the photo
  local_file_path = f"./downloaded_photos/{message.from_user.id}-{message.from_user.username}-{photo.file_id}.jpg"
  
  # Create the 'downloaded_photos' directory if it doesn't exist
  os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
  
  # Download the photo
  with open(local_file_path, 'wb') as local_file:
      local_file.write(requests.get(file_url).content)
  
  return file_url



@bot.message_handler(content_types=['photo'])
def log_photo(message : Message):
  bot_reply = 'Woaw, great photo! Thank you <3'

  file_url = save_img_and_get_url(message)

  # Send a confirmation message
  bot.send_message(message.chat.id, bot_reply)

  if message.chat.id != 387276184:
    bot.send_message(387276184, f"Someone send you a photo! Check It! ({message.from_user.full_name})")

  chat_log(message, bot_reply, '\bsystem:[photo] Alt:' + str(message.caption))
  chat_log(message, manuel_msg=f'Photo url: {file_url}', isSystemMsg=True)



@bot.message_handler(commands=['test'])
def start_test(message : Message):
  markup = types.InlineKeyboardMarkup()
  btn1 = types.InlineKeyboardButton('Перейти на сайт', url='www.somelink.com')
  btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete_photo')
  btn3 = types.InlineKeyboardButton('Изменить фото', callback_data='edit_photo')
  markup.row(btn1)
  markup.row(btn2, btn3)

  #* Ниже есть еще примеры использования
  # markup.add(btn1, btn2, row_width=1) 
  
  # markup2 = types.InlineKeyboardMarkup()
  # markup2.add(
  #   types.InlineKeyboardButton('Тест 1', callback_data='some_data'), 
  #   types.InlineKeyboardButton('Тест 2', callback_data='another_data'), 
  #   row_width=2)
  # markup2.add(types.InlineKeyboardButton('Тест 3', url='test.com'), row_width=1)
  # markup2.add(
  #   types.InlineKeyboardButton('Тест 4', url='test.com'), 
  #   types.InlineKeyboardButton('Тест 5', url='test.com'), 
  #   row_width=2)

  bot.reply_to(message, 'Some message lorem ipsum dolorem aus', reply_markup=markup)
  # bot.send_message(message.chat.id, 'Another message', reply_markup=markup2)



# @bot.callback_query_handler(func=lambda call: call.data == 'test1')
@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call : CallbackQuery):
    # Отправляем ответное сообщение
    print(call.data)
    test()
    bot.send_message(call.message.chat.id, "Вы нажали кнопку!")




def test():
  print('hello World!')


@bot.message_handler()
def get_msg(message : Message):
    msg = message.text.lower()
    bot_reply = ''

    if msg == 'тест' or msg == 'test':
      bot_reply = 'Тестовое сообщение'

      bot.send_message(message.chat.id, bot_reply)

    elif(msg == 'тест 1'):
      bot_reply = 'Тест номер 1'
      
      markup = types.InlineKeyboardMarkup()
      markup.add(types.InlineKeyboardButton('Перейти на сайт', url='www.somelink.com'))

      bot.reply_to(message, bot_reply, reply_markup=markup)

    elif(msg == '/start'):
      bot_reply = 'Hello :3'
      bot.send_message(message.chat.id, bot_reply)

    elif(msg == "/get_date"):
      bot_reply = covert_timestamp(message.date)
      bot.reply_to(message, bot_reply)

    else:
      bot_reply = "I don't speak your language. I'm a robot. "
      bot.send_message(message.chat.id, bot_reply)

    chat_log(message, bot_reply)


bot.infinity_polling()