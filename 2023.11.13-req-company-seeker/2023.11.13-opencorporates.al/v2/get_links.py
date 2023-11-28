from requests_html import HTMLSession

session = HTMLSession()

with open('links.txt', 'a') as file:
  for i in range(1, 709):
    url = f'https://www.opencorporates.al/sq/search?fjal_k=import&page={i}'

    response = session.get(url)

    # Рендеринг JavaScript
    response.html.render()

    # Парсинг страницы после рендеринга
    a_tags = response.html.find('a.btn.btn-danger.text-uppercase.font-weight-bold.d-lg-block')
    print('Page no: ', i)
    for idx, tag in enumerate(a_tags):
        file.write(f'{tag.attrs["href"]}\n')
        print(str(idx), tag.attrs['href'])
