# import requests

# for i in range (76):
#   req = requests.get('https://yellowpages.com.eg/en/map-category/marble-&-granite/p73')
#   req.


import requests
from bs4 import BeautifulSoup

for i in range(1, 76):
  # URL веб-страницы, которую вы хотите анализировать
  url = f'https://yellowpages.com.eg/en/map-category/marble-&-granite/p{i}'

  # Отправляем HTTP-запрос и получаем ответ
  response = requests.get(url)

  # Проверяем, что запрос был успешным
  if response.status_code == 200:
      with open('links.md', 'a') as file:
        # Используем BeautifulSoup для анализа HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем div с нужным классом
        search_results = soup.find_all('div', class_='search-result-div-map-view map-search-results')

        # В каждом найденном div ищем дочерние div с нужным классом и извлекаем ссылки
        for result in search_results:
            item_rows = result.find_all('div', class_='row item-rowmap content-widget')
            for item in item_rows:
                link = item.find('a', href=True)
                if link:
                    print(link['href'])
                    file.write(f"https:{link['href']}\n")
  else:
      print(f'Failed to retrieve web page. Status code: {response.status_code}')
  