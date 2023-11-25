import time
import requests
from bs4 import BeautifulSoup
import json

# URL для запроса
url = 'https://www.orgpage.ru/penza/mango-mebel-mebelnaya-kompaniya-2190410.html'

req_no = 37
excludeIdList = ['836322']

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru,tr-TR;q=0.8,tr;q=0.6,en-US;q=0.4,en;q=0.2',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.orgpage.ru/rossiya/mebel-2/'
    # Добавьте ещё заголовки при необходимости
}

# Отправка запроса
response = requests.get(url)

# Обработка ответа
if response.status_code == 200:
    html_content = response.text
      # предполагая, что ответ в формате JSON
    file = open('htmltext.txt', 'w')
    print(html_content)
    file.write(str(html_content))