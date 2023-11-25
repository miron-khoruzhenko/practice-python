import requests
import json

# URL для запроса
url = 'https://www.orgpage.ru/Rubricator/ajax/RubricatorRegionLevel2Next/'

# Параметры запроса
params = {
    'rubricId': 12852,
    'rubricLevel': 2,
    'excludeIdList': '',
    # 'excludeIdList': '836322,1236584,958859,2504640,2520206,1964181,2473609,1544115,1028326,5368020,2115783,2510066,5398603,2436150,5554523,2473152,2426501,2563576,1547492,2496736,2195810,16758,2472558,2540066,2690374,1401639,6113727,1604035,2545717,24801',
    'countryId': 1,
    'count': 500,
    'offsetNum': 1
}

# Заголовки запроса
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru,tr-TR;q=0.8,tr;q=0.6,en-US;q=0.4,en;q=0.2',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.orgpage.ru/rossiya/mebel-2/'
    # Добавьте ещё заголовки при необходимости
}

# Отправка запроса
response = requests.get(url, headers=headers, params=params)

# Обработка ответа
if response.status_code == 200:
    data = response.json()  # предполагая, что ответ в формате JSON
    print("Удачно")  # или любая другая обработка
    file = open('text.md', 'w')
    file1 = open('text1.json', 'w')

    file.write(str(data))
    json.dump(data['PartialView'], file1)

else:
    print("Ошибка при запросе:", response.status_code)
