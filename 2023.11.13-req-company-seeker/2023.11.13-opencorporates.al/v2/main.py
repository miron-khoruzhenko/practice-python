from requests_html import HTMLSession
from bs4 import BeautifulSoup
import xlsxwriter as xl
import requests
import time
import json
import re




def get_data_from_id(url, session):
  email   = 'None'
  tel     = 'None'
  urls    = 'None'
  name    = 'None'

  response = session.get(f'https://opencorporates.al{url}')
  response.html.render(timeout=10)

  html_text = response.html.text
  name = html_text.split('\n')[0]


  urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', html_text)
  # print(urls)
  tmp_url = []
  for url in urls:
    if 'google' in url:
      continue
    tmp_url.append(url)
  urls = ', '.join(tmp_url)

  try:
    email = re.search(r'Adresa Email\n(.+)', html_text).group(1)
  except:
    pass
  try:
    tel = re.search(r'Telefoni\n(.+)', html_text).group(1)
  except:
    pass

  return [name, urls, email, tel]



def get_links_from_file(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()
    url_arr = []

    for line in lines:
      url_arr.append(line[:-1])
    
  return url_arr



if __name__ == '__main__':
  index = 1
  from_index = 0 #! <<<<<<<<<<<<<<<<<
  # to_index = 300

  session = HTMLSession()

  try:
    url_ids = get_links_from_file('links1.txt')

    url_ids_len = len(url_ids)


      #* ТУТ ======================================================
    for index, id in enumerate(url_ids[from_index:]): #* <<<<<<
    #* ТУТ ======================================================

      index += from_index
      startTime = time.time()
      # for data in get_data_from_id(id):
      try:
        data = get_data_from_id(id, session)
      except Exception as e:
        with open(f'error.txt', 'a') as errorFile:
          errorFile.write(f'Index: {index} \nError: {e}')
          print(e)
        continue

      with open(f'./dist/companies.txt', 'a') as file:
        file.write(f'Index: {index}\n')
        file.write(f' Name: {str(data[0])}\n')
        file.write(f'  URL: {str(data[1])}\n')
        file.write(f'Email: {str(data[2])}\n')
        file.write(f'Phone: {str(data[3])}\n')
        file.write(f'   ID: {str(id)[-10:]}\n\n')

      print(f'Index: {index}')
      print(f' Name: {str(data[0])}')
      print(f'  URL: {str(data[1])}')
      print(f'Email: {str(data[2])}')
      print(f'Phone: {str(data[3])}')
      print(f'   ID: {str(id)[-10:]}\n')

      index += 1
  except Exception as e:
    print(e)



