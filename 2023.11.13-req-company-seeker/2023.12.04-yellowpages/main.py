import requests
from bs4 import BeautifulSoup
import time
# # # 1 - 75

start_time1 = time.time()

links_arr = []
links_ids = []

with open('links.md', 'r') as file:
  lines = file.readlines()
  for line in lines:
    if 'https:' in line:
      links_arr.append(line[:-1])
      links_ids.append(line.split('/')[-1][:-1])

for index, link in enumerate(links_arr):
  start_time2 = time.time()

  name = ''
  whatsapp = ''
  website = ''
  phones = ''

  response = requests.get(link)

  if response.status_code != 200:
    break

  with open('info.md', 'a') as file:

    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find('h1', class_='companyName')
    if name:
      name = name.text
      file.write(f"    Name: {name}\n")
    else:
      file.write(f"    Name: \n")


    whatsapp = soup.find('a', class_='whatsapp')
    if whatsapp:
      whatsapp = whatsapp['href'].split('phone=')[-1]
      file.write(f"Whatsapp: {whatsapp}\n")
    else:
      file.write(f"Whatsapp: \n")
    
    website = soup.find('a', class_='website')
    if website:
      website = website['href']
      file.write(f" Website: {website}\n")
    else:
      file.write(f" Website: \n")

    res = requests.get(f'https://yellowpages.com.eg/en/getPhones/{links_ids[index]}/false')
    temp = res.text.replace('[', '').replace(']', '').replace('"', '').strip().split(',')
    file.write('  Phones: ')
    for tmp in temp:
      if len(tmp) > 1:
        file.write(f"{tmp} ")
    file.write('\n')

    file.write(f"    Link: {link}\n\n")

    print('==================================`')
    print(f'Index {index} of {len(links_arr)}\n')
    print(f'    Name: {name}')
    print(f' Website: {website}')
    print(f'Whatsapp: {whatsapp}')
    print(f'  Phones: {temp}')
    print(f'Req time: {time.time() - start_time2}')
    print(f'All time: {time.time() - start_time1}')
    print('==================================`')
