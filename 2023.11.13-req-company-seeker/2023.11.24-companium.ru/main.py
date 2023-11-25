from requests_html import HTMLSession
from bs4 import BeautifulSoup
from typing import List
import xlsxwriter as xl
import time
import json
import re

import urllib.request


from lxml import html, etree
import requests



# links = [
#   'https://companium.ru/id/1227700368279-moskovskoe-prop',
#   'https://companium.ru/id/1107746941720-stenteks',
#   'https://companium.ru/id/1027739064528-dzhii-hehlskea',
#   'https://companium.ru/id/1127746016507-mpo-metallist'
# ]

# names = [
#   'АО "МОСКОВСКОЕ ПРОП"',
#   'ООО "СТЕНТЕКС"',
#   'ООО "ДЖИИ ХЭЛСКЕА"',
#   'АО "МПО "МЕТАЛЛИСТ"',
# ]


def get_links_from_file(filename):
  links_arr = []
  with open(filename, 'r') as file:
    lines = file.readlines()

    for line in lines:
      links_arr.append(line[6:-1])
  return links_arr




def get_ids_from_urls(link_arr : List[str]):
  id_arr = []
  for link in link_arr:
    start_id_index = link.find('id/') + 3
    last_id_index = link.find('-')

    id_arr.append(link[start_id_index : last_id_index])

    

  return id_arr




def get_data_from_id(id):
    name_xpath = f"//a[contains(@href, 'http://companium.ru/id/')]/span"
    phone_xpath = "//*[contains(@id, 'copy-phone-')]"
    email_xpath = "//*[contains(@id, 'copy-email-')]"
    website_xpath = "//strong[contains(text(), 'Веб-сайт')]/following-sibling::node()"
    social_xpath = "//strong[contains(text(), 'Cоциальные сети')]/following-sibling::node()"

    url = f'https://companium.ru/id/{id}/contacts'

    with urllib.request.urlopen(url) as response:
        content = response.read()
        tree = html.fromstring(content.decode('utf-8'))

    def get_text(xpath):
        elements = tree.xpath(xpath)
        texts = []
        for element in elements:
            if hasattr(element, 'text') and element.text:
                texts.append(element.text.strip())
                # texts.append(element.text)
            elif isinstance(element, str):
                texts.append(element.strip())
                # texts.append(element)
        return '     '.join(texts)

    name_text     = get_text(name_xpath)
    website_text  = get_text(website_xpath)
    social_text   = get_text(social_xpath)
    phones        = get_text(phone_xpath)
    emails        = get_text(email_xpath)

    return name_text, phones, emails, website_text, social_text, url








if __name__ == '__main__':
  # index = 0
  from_index = 13456 #! <<<<<<<<<<<<<<<<<
  # to_index = 600
  links = get_links_from_file('./links.txt')

  url_ids = get_ids_from_urls(links)
  url_ids_len = len(url_ids)

  with open(f'test.txt', 'a') as file:

    for index, id in enumerate(url_ids[from_index:]):

      index += from_index
      startTime = time.time()
      try:
        data = get_data_from_id(id)
      except Exception as e:
        with open('error.txt', 'a') as errorfile:
          errorfile.write(f"Index: {index}\n")
          errorfile.write(f"   ID: {id}\n")
          errorfile.write(f"Error: {e}\n\n")
        print("Error", e)
        continue
      
      print(f'   Index: {index} / {url_ids_len - 1}')
      print(f'    Name: {f"{str(data[0])[:40]}..." if len(data[0]) > 40 else str(data[0])}')
      print(f'   Phone: {f"{str(data[1])[:40]}..." if len(data[1]) > 40 else str(data[1])}')
      print(f'   Email: {f"{str(data[2])[:40]}..." if len(data[2]) > 40 else str(data[2])}')
      print(f' Website: {f"{str(data[3])[:40]}..." if len(data[3]) > 40 else str(data[3])}')
      print(f' Socials: {f"{str(data[4])[:40]}..." if len(data[4]) > 40 else str(data[4])}')
      print(f'    Time: {time.time() - startTime}\n\n')

      if len(data[1]) < 3 and len(data[2]) < 3 and len(data[3]) < 3 and len(data[4]) < 3:
        print('^^^ Skiped ^^^\n\n')
        continue

      file.write(f'   Index: {index}\n')
      file.write(f'    Name: {str(data[0])}\n')
      file.write(f'   Phone: {str(data[1])}\n')
      file.write(f'   Email: {str(data[2])}\n')
      file.write(f' Website: {str(data[3])}\n')
      file.write(f' Socials: {str(data[4])}\n')
      file.write(f'Data URL: {str(data[5])}\n\n\n')

