import urllib.request
from lxml import html, etree
import time

def get_links_from_table(url):
    xpath = "//table[@class='table table-lg']/tbody/tr//a/@href"
    links_arr = []

    with urllib.request.urlopen(url) as response:
        content = response.read()
        tree = html.fromstring(content.decode('utf-8'))

    links = tree.xpath(xpath)
    for link in links:
      links_arr.append(link)
    return links_arr


with open('links.txt', 'a') as file:
  for i in range(1,414):
    #https://companium.ru/select?code=464600
    url = f'https://companium.ru/select?code=464600&page={i}'
    
    links = get_links_from_table(url)

    for index, link in enumerate(links):
      link_str = f'{str(i).zfill(2)}.{str(index).zfill(2)} {link}\n'
      print(f'saved: {link_str}')
      file.write(link_str)
    time.sleep(1)
