import socket
import time

HOST = 'localhost'  # Адрес, на котором запущена программа B
PORT = 12300        # Порт для соединения с программой B

print("stop     - stop program")
print("details  - show/hide details")
print("backup   - creating backup")

while True:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      # data_to_send = "Данные для отправки"
      try:
        s.connect((HOST, PORT))
      except:
        time.sleep(2)
        continue
      data_to_send = input()

      s.send(data_to_send.encode())
      print('Sended')