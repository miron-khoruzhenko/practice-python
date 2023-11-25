from bs4 import BeautifulSoup

# Открываем и читаем HTML файл
with open('text1.html', 'r', encoding='utf-8') as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')

# Список для сохранения информации
data = []

# ','.join(str(i) for i in list1)

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
    data.append((data_companyid, link))

# Вывод собранных данных
with open("links.txt", "a") as myfile1:
    with open("excluded.txt", "a") as myfile2:
        for companyid, link in data:
            print("data-companyid:", companyid, "Ссылка:", link)
            myfile1.write(f"{link}\n")
            myfile2.write(f"{companyid}\n")
