from requests_html import HTMLSession
from bs4 import BeautifulSoup
import xlsxwriter as xl
import requests
import time
import json
import re




def get_id_urls(api):
  response = requests.get(api)

  data = json.loads(response.content)

  # Получение значения ключа "data"
  data_value = data['data']
  id_arr = []
  names_arr = []

  for data in data_value:
    id_arr.append(data['NIPT'])
    names_arr.append(data['name'])

  return (id_arr, names_arr)




def get_data_from_id(id, session):
  email   = 'None'
  tel     = 'None'
  urls    = 'None'
  name    = 'None'

  response = session.get(f'https://opencorporates.al/sq/nipt/{id}')
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



# api = 'https://opencorporates.al/sq/rindertimicompany/any?draw=3&columns[0][data]=NIPT&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=name&columns[1][name]=name&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=administrator&columns[2][name]=administrator&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=district&columns[3][name]=district&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=capital&columns[4][name]=capital&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=partner&columns[5][name]=partner.name&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&order[0][column]=0&order[0][dir]=asc&start=0&length=-1&search[value]=&search[regex]=false&_=1699931698658'

# 600
# api = 'https://opencorporates.al/sq/company/any?draw=2&columns[0][data]=NIPT&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=name&columns[1][name]=name&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=administrator&columns[2][name]=administrator&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=district&columns[3][name]=district&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=capital&columns[4][name]=capital&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=partner&columns[5][name]=partner.name&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&order[0][column]=0&order[0][dir]=asc&start=0&length=-1&search[value]=&search[regex]=false&_=1699972000975'

# https://opencorporates.al/sq/companyfrom2016
api = 'https://opencorporates.al/sq/companyfrom2016/any?draw=2&columns[0][data]=NIPT&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=name&columns[1][name]=name&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=administrator&columns[2][name]=administrator&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=district&columns[3][name]=district&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=capital&columns[4][name]=capital&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=partner&columns[5][name]=partner.name&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&order[0][column]=0&order[0][dir]=asc&start=0&length=-1&search[value]=&search[regex]=false&_=1699985429196'


if __name__ == '__main__':
  index = 1
  from_index = 0 #! <<<<<<<<<<<<<<<<<
  to_index = 300

  excel = xl.Workbook(f'opencorporate{int(index / 2)}-Time:{time.time()}.xlsx')
  spreadsheet = excel.add_worksheet()
  session = HTMLSession()

  try:
    url_ids, name_arr = get_id_urls(api)
    #TODO: Time passed
    #TODO: Index of ALLINDEX
    url_ids_len = len(url_ids)

    #* ТУТ ======================================================
    for index, id in enumerate(url_ids[from_index:to_index]): #* <<<<<<
    #* ТУТ ======================================================

      index += from_index
      startTime = time.time()
      # for data in get_data_from_id(id):
      try:
        data = get_data_from_id(id, session)
      except Exception as e:
        print(e)
        continue
      with open(f'test1.txt', 'a') as file:
        # file.write(f'{index} name: {name_arr[index]} url: {str(data[1])} email: {str(data[2])} tel : {str(data[3])} { "id: " + str(id)}\n\n')
        file.write(f'{index} {name_arr[index]} {str(data[1])} {str(data[2])} {str(data[3])} { "id: " + str(id)}\n\n')
#
        # file.write(f'{index} {name_arr[index]} {str(data[1])} {str(data[2])} {str(data[3])} { "id: " + str(id)}\n\n')
      spreadsheet.write(f'A{index}', name_arr[index])
      spreadsheet.write(f'B{index}', str(data[1]))  
      spreadsheet.write(f'C{index}', str(data[2]))
      spreadsheet.write(f'D{index}', str(data[3]))
      spreadsheet.write(f'E{index}', 'id: ' + str(id))

      print(f'Company: {id} \nName: {name_arr[index]} \nIndex: {index + 1} of {url_ids_len} Time: {time.time() - startTime}\n\n')
      index += 1
  except Exception as e:
    print(e)
    excel.close()

  excel.close()



