import time
import requests
from bs4 import BeautifulSoup
import json
import xlsxwriter as xl



# URL для запроса
url = 'https://www.orgpage.ru/Rubricator/ajax/RubricatorRegionLevel2Next/'

req_no = 1
excludeIdList = ['836322']
countPerCall = 500
index = 1

excel = xl.Workbook(f'orgpage{req_no}.xlsx')
spreadsheet = excel.add_worksheet()

while True:
    # Параметры запроса
    # if req_no * countPerCall % 5000 == 0:
    #     excel.close()
    #     excel = xl.Workbook(f'orgpage{req_no}.xlsx')
    #     spreadsheet = excel.add_worksheet()

    params = {
        'rubricId': 12852,
        'rubricLevel': 2,
        'excludeIdList': '836322',
        # 'excludeIdList': '836322,1236584,958859,2504640,2520206,1964181,2473609,1544115,1028326,5368020,2115783,2510066,5398603,2436150,5554523,2473152,2426501,2563576,1547492,2496736,2195810,16758,2472558,2540066,2690374,1401639,6113727,1604035,2545717,24801',
        # 'excludeIdList': ','.join(str(i) for i in excludeIdList),
        'countryId': 1,
        'count': countPerCall,
        'offsetNum': req_no
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
        responseData = response.json()  # предполагая, что ответ в формате JSON
        print("Удачно. Дальше?", responseData['hasNext'])  # или любая другая обработка
        # with open(f'text{req_no}.json', 'w') as file:
        #     json.dump(responseData, file)


        soup = BeautifulSoup(responseData['PartialView'], 'html.parser')

        # Список для сохранения информации
        companyData = []

        # Находим все элементы div с классом similar-item
        similar_items = soup.find_all('div', class_='similar-item')

        for item in similar_items:
            # Получение data-companyid для каждого элемента
            data_companyid = item.get('data-companyid')

            # Находим div с классом similar-item__title внутри текущего similar-item
            title_div = item.find('div', class_='similar-item__title')
            
            # Извлекаем ссылку, если она существует
            link = title_div.find('a')['href'] if title_div and title_div.find('a') else None

            # Добавляем собранную информацию в список
            companyData.append((data_companyid, link))

            name = item.find('div', class_='similar-item__title').get_text(strip=True)
            spreadsheet.write(f'A{index}', name)
            index += 1
            info = item.find('div', class_='similar-item__phone').get_text(strip=True)
            spreadsheet.write(f'A{index}', info)
            index += 1
            index += 2

        with open("links.txt", "a") as linksFile:
            with open("excluded.txt", "a") as exclFile:

                for companyid, link in companyData:
                    print("offset", req_no, "queue", req_no * countPerCall, "data-companyid:", companyid, "Ссылка:", link)
                    excludeIdList.append(companyid)

                    linksFile.write(f"{link}\n")
                    exclFile.write(f"{companyid}\n")
    
        # # Вывод собранных данных
        # for companyid, link in data:
        #     print("data-companyid:", companyid, "Ссылка:", link)
        
        if not responseData['hasNext']:
            break
        req_no += 1

        time.sleep(1)



    else:
        print("Ошибка при запросе:", response.status_code)

        if response.status_code == 500:
            countPerCall = int(countPerCall/2)
            req_no *= 2
excel.close()
