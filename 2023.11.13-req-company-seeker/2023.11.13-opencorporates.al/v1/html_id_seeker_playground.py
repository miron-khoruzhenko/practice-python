# import requests
# from bs4 import BeautifulSoup


# def get_html(url):
#   response = requests.get(url)
#   if response.status_code != 200:
#     return 'Error'
  
#   soup = BeautifulSoup(response.content,"html.parser")
#   print(soup)
#   con = soup.find("td", attrs={"class": "sorting_1"})
#   con = con.find("a")
  
#   return con.text.strip()

# tmp = get_html('https://opencorporates.al/sq/rindertimicompany')

# print(tmp)
# !=========================

# from bs4 import BeautifulSoup
# from selenium import webdriver

# url = "https://opencorporates.al/sq/rindertimicompany"
# browser = webdriver.PhantomJS()
# browser.get(url)
# html = browser.page_source
# soup = BeautifulSoup(html, 'html.parser')
# con = soup.find("td", attrs={"class": "sorting_1"})
# print(con)
# # a = soup.find('section', 'wrapper')

# ! ==========================
# from requests_html import HTMLSession

# session = HTMLSession()
# response = session.get('https://opencorporates.al/sq/rindertimicompany')
# response.html.render()  # Выполняет JavaScript

# # Теперь можно извлекать данные с отрендеренной страницы
# tmp=[]
# a_elements = response.html.find('td.sorting_1 a')
# for a_element in a_elements:
#   print(a_element.text)
#   tmp.append(a_element.text)
# print(tmp)

# !========================

import requests
import json
from bs4 import BeautifulSoup
import re

# response = requests.get('https://opencorporates.al/sq/rindertimicompany/any?draw=3&columns[0][data]=NIPT&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=name&columns[1][name]=name&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=administrator&columns[2][name]=administrator&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=district&columns[3][name]=district&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=capital&columns[4][name]=capital&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=partner&columns[5][name]=partner.name&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&order[0][column]=0&order[0][dir]=asc&start=0&length=-1&search[value]=&search[regex]=false&_=1699931698658')

# data = json.loads(response.content)

# # Получение значения ключа "data"
# data_value = data['data']
# id_arr = []

# for data in data_value:
#   id_arr.append(data['NIPT'])

# from requests_html import HTMLSession

# session = HTMLSession()
# response = session.get('https://opencorporates.al/sq/nipt/J61924002T')
# response.html.render()  # Выполняет JavaScript

# # Теперь можно извлекать данные с отрендеренной страницы
# tmp=[]
# a_elements = response.html.find('td.sorting_1 a')
# for a_element in a_elements:
#   print(a_element.text)
#   tmp.append(a_element.text)
# print(tmp)


# response = requests.get(f'https://opencorporates.al/sq/nipt/{id_arr[0]}')
# response = requests.get(f'https://opencorporates.al/sq/nipt/J61924002T')
# soup = BeautifulSoup(response.content,"html.parser")

# th_adresa = soup.find('th', string='Adresa:')

# if th_adresa:
#     # Находим родительский элемент <tr>
#     parent_tr = th_adresa.find_parent('tr')

#     if parent_tr:
#         # Находим следующий элемент <td> после <th>
#         td_adresa = parent_tr.find('td')
#         if td_adresa:
#             # Выводим текст элемента <td>
#             text = td_adresa.get_text()
#             urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', text)

#             if urls:
#                 print("Найденные URL-адреса:")
#                 for url in urls:
#                     print(url)

#             # Поиск элементов с ID telList и emailList
#             tel_list = td_adresa.find(id='telList')
#             email_list = td_adresa.find(id='emailList')

#             if tel_list:
#                 print("Телефонные номера:", tel_list.text.strip())
#             if email_list:
#                 print("Электронные адреса:", email_list.text.strip())
#             # print("Найденный адрес:", td_adresa.text.strip())
#         else:
#             print("Соседний элемент <td> не найден")
#     else:
#         print("Родительский элемент <tr> не найден")
# else:
#     print("Элемент <th> с текстом 'Adresa:' не найден")

# telList
# id="emailList"
# https://opencorporates.al/sq/nipt/J61812013R
# print(id_arr)
# print(len(id_arr))


response = requests.get('https://opencorporates.al/sq/rindertimicompany/any?draw=3&columns[0][data]=NIPT&length=-1')
print(response.text)