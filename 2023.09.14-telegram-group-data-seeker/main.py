from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement

import time

import sys
from io import TextIOWrapper
import os
import re
import requests

from unidecode import unidecode

class DriverOptions:
  def __init__(self):
    self.driver = 0
    self.wait = 0
    self.setup_driver()
      
  
  def setup_driver(self):
      # options = FirefoxOptions()
    options = Options()

    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_experimental_option("detach", True)


    # self.driver = Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()), options=options)
    self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

    self.driver.implicitly_wait(5)
    # Для работы в режиме headless
    self.driver.set_window_size(1440, 900) 


    self.wait = WebDriverWait(self.driver, 3)
    self.driver.maximize_window()

  def wait_clickable(self, by, path):
    return (self.wait.until(
      EC.element_to_be_clickable((by, path))
    ))

  def wait_located(self, by, path):
    return (self.wait.until(
      EC.presence_of_element_located((by, path))
    ))

  def driver_test(self):
    self.driver.get('http://example.com/')
    print(self.driver.title)



# class DataScrabing():
class DataScrabing(DriverOptions):
  def __init__(self):
    super().__init__()
    self.file : TextIOWrapper = None
    self.links_file_lines = ""
    self.index = 0
    self.previous_name = ''
    self.imgIndex = 1



  def start(self):
    self.get_liks_from_file('links.md')
    self.operate_lines()



  def get_liks_from_file(self, name):
    try:
      with open(name, 'r') as file:
        self.links_file_lines = file.readlines()
    except Exception as e:
      print('Ошибка что то пошло не так при попытке открытии файла. Ошибка:\n', e)
      quit()



  def operate_lines(self):
    for line in self.links_file_lines:
      # print(line[0:5], end='\n')
      if ('-' in line[0:1]):
        name = line[2:-1]
        self.handle_file_creation(name)

      elif ("http" in line[0:5]):
        self.handle_url(line.strip())

      elif("END" in line):
        self.handle_file_creation("END")

      else:
        continue



  def handle_file_creation(self, filename : str):
    filename = filename
    print(f'\n\n =============== File Created {filename} ===============\n\n')

    if(not filename):
      filename = 'noname' + str(time.time())
    else:
      filename = unidecode(filename.strip()).lower()
      filename = self.handle_sepcial_signs(filename)


    if(self.file):
      if(self.previous_name):
        self.file.write(f']\n\nexport default {self.previous_name};')
      else:
        self.file.write(f']\n\nexport default {filename};')

      self.file.close()
      # print("File Closed", self.file)


    if('data' not in os.listdir()):
      os.mkdir('./data')
    if('img' not in os.listdir()):
      os.mkdir('./img')

    if ("end" != filename):
      self.file = open(f"./data/{self.index}.{filename}.ts", 'w')
      self.file.write(f"let index = 0;\n\nconst {filename} = [\n")
      self.index += 1
      self.previous_name = filename




  def handle_sepcial_signs(self, input_string):
    special_characters_pattern = r'[\\/:"*?<>|\s]'
    replaced_string = re.sub(special_characters_pattern, '_', input_string)
    
    return replaced_string



  def handle_url(self, url):
    dataArr = self.get_data_from_web(url)
    if(dataArr):
      self.create_json(*dataArr)
    # self.create_json('test', 'somebigtext', 'img', 'www.somelink.com')
    pass



  def get_data_from_web(self, url):
    self.driver.get(url)
    print('URL: ', url)

    
    try:
      headingWE : WebElement = self.wait_located(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/span')
    except Exception as e:
      with open('errors.md', a) as file:
        file.write(f'NO HEADING: Error. Link may be expired')
      return()
    try:
      descrWE   : WebElement = self.wait_located(By.CLASS_NAME, 'tgme_page_description')
    except Exception as e:
      descrWE = ''
    imgWE     : WebElement = self.wait_located(By.CLASS_NAME, 'tgme_page_photo_image')
    extraWE   : WebElement = self.wait_located(By.CLASS_NAME, 'tgme_page_extra')

    heading : str = headingWE.get_attribute('innerText').replace('"', "'")
    descr   : str = descrWE and descrWE.get_attribute('innerHTML').replace('"', "'")
    members : str = extraWE.get_attribute('innerText').split(', ')[0]
    imgLink : str = imgWE.get_attribute('src')
    imgSrc  : str = f"./img/img{str(self.imgIndex).zfill(3)}.png"

    self.imgIndex += 1

    # self.driver.get(imgLink)
    # self.driver.save_screenshot(imgSrc)

    try:
      response = requests.get(imgLink)

      if response.status_code == 200:
          with open(imgSrc, 'wb') as file:
              file.write(response.content)
      else:
          print("Не удалось загрузить изображение.")
    except Exception as e:
      with open('errors.md', 'a') as file:
        file.write(f'LOADING ERROR: {url} \n \t{e}')
      print(f"Ошибка при загрузку изображения", e)

    return([heading, descr, imgSrc, url, members])



  def create_json(self, heading='', descr='', img='', href='', members=''):
    if(not self.file):
      print('Something went wrong when creating json. File should be open but it not.')
      quit()
    
    jsonStr = str("\t{\n"
      f'\t\theading : "{heading}",\n'
      f'\t\tdescr : "{descr}",\n'
      f'\t\timg : "{img}",\n'
      f'\t\tmembers : "{members}",\n'
      f'\t\thref : "{href}",\n'
      f'\t\tindex : index++,\n'
    "\t},\n")

    print(f'DONE: {heading} - {href}')


    self.file.write(jsonStr)
    






if __name__ == '__main__':
    bot = DataScrabing()
    bot.start()
