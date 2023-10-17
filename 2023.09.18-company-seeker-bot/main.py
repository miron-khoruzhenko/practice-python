from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from datetime import datetime
import driverSetup
import threading
import requests
import socket
import time
import sys
import os
import re

import xlsxwriter as xl


# TODO: connection loss => refresh
# TODO: program crash => save and restart

# class DataScrabing():
class DataScrabing(driverSetup.DriverOptions):
  def __init__(self):
    super().__init__()
    
    self.excel = None 
    self.spreadsheet = None
    self.index = 1
    self.pageNumber = 158
    self.lastPageNumber = 169
    self.filename = f'./140online-{self.pageNumber}-({datetime.now()}).xlsx'
    self.link = ''

    self.isQuitRequied = False
    self.showDetails = True
    self.conn = False

    # self.test = 20


  def start(self):
    print('Starting...')

    

    self.excel = xl.Workbook(self.filename)
    self.spreadsheet = self.excel.add_worksheet()

    result_thread = threading.Thread(target=self.start_socket_server)
    result_thread.start()
    while not self.conn:
      print('wait...')
      time.sleep(1) 

    self.open_adblock()

    while True:

      try:
        container = self.get_data_container()
        self.operate_foreach_of(container)
      except Exception as e:
        self.driver.save_screenshot(f'{time.time()}-error.png')

        print('Error: ', e)
        break
    self.excel.close()



  def start_socket_server(self):
    HOST = 'localhost'  # Адрес, на котором запущена программа B
    PORT = 12300        # Порт для соединения с программой B

    self.conn = False

    while not self.conn:
      try:
        print('Попытка создания сокета')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
          s.bind((HOST, PORT))

          s.listen()
          print('Успешно')

          
          while True:
            self.conn, addr = s.accept()

            with self.conn:
              # print('Соединение установлено с', addr)
              received_data = self.conn.recv(1024).decode()

              if received_data.lower() == 'stop':
                self.isQuitRequied = True
                quit()
              elif received_data.lower() == 'details':
                self.showDetails = not self.showDetails
              elif received_data.lower() == 'backup':
                self.excel.close()
                self.filename = f'./140online-{self.pageNumber}-({datetime.now()}).xlsx'
                self.excel = xl.Workbook(self.filename)

              # print('Приняты данные:', received_data)
      except:
        print('Ошибка создания сокета...')
        time.sleep(2)
        # PORT += 1



  def open_adblock(self):
    self.driver.get('about:blank')

    startTime = time.time()

    while len(self.driver.window_handles) == 1 and time.time() - startTime < 5:
      pass

    while len(self.driver.window_handles) > 1:
      self.driver.switch_to.window(self.driver.window_handles[-1])
      self.driver.close()
      self.driver.switch_to.window(self.driver.window_handles[0])


  def get_data_container(self):
    if(self.lastPageNumber and self.pageNumber > self.lastPageNumber):
      raise Exception('Last Page Finished')
    

    # self.link = f'https://www.140online.com/class/pages/En/207/{self.pageNumber}/Gypsum/'
    self.link = f'https://www.140online.com/class/pages/En/193/{self.pageNumber}/General%20Contractors/'

    # self.driver.get(self.link + f'&page={self.pageNumber}')
    self.driver.get(self.link)

    # try:
    #   self.wait_clickable(By.ID, 'dismiss-button').click()
    # except:
    #   pass


    dataContainer = self.driver.find_elements(By.CSS_SELECTOR, '#resultView .row-fluid')

    # adBlockLeft = self.wait_located(By.ID, 'left_Banner')
    # adBlockLeft.parentNode.removeChild(adBlockLeft)
    # adBlockTop = self.wait_located(By.XPATH, '//*[@id="form1"]/div[7]/div[2]')
    self.pageNumber += 1
    # time.sleep(6000)
    print('\n========== New Page ==========\n')

    return dataContainer
  


  # def remove_ads()



  def operate_foreach_of(self, container):
    arrLen = len(container)

    for index, item in enumerate(container):
      self.open_pages(item)

    for index, item in enumerate(container):
      if self.isQuitRequied:
        raise Exception('Leaving program')

      self.excel_write_companydata(
        self.get_company_data(item, index, arrLen)
      )



  def open_pages(self, element):
    try:
      link = element.find_element(By.CSS_SELECTOR, '.tith3 a')
      link.send_keys(Keys.CONTROL + Keys.RETURN)

    except:
      return



  def get_company_data(self, element : WebElement, index, arrLen):
    # print('Get Company Data - ', end='')
    startTime = time.time()

    name = ''
    address = ''
    phone = ''
    website = ''
    email = ''

    # facebook = ''
    # instagram = ''
    whatsapp = ''
    anotherData = ''

    try:
      # link = element.find_element(By.CSS_SELECTOR, '.tith3 a')
      # link.send_keys(Keys.CONTROL + Keys.RETURN)
      self.driver.switch_to.window(self.driver.window_handles[-1])

    except:
      return


    try:
      phone = self.wait_located(By.ID, f'ctl09_lblTel').get_attribute('innerText')

    except:
      phone = 'No Phone'

    try:
      table = self.driver.find_elements(By.CSS_SELECTOR, 'table.iconcomp')
      # print(table)
      for row in table:
        if row.get_attribute('innerHTML') != '':
          website = self.wait_located(By.ID, 'ctl09_lnkwebsite').get_attribute('href')
          email = self.wait_located(By.ID, 'ctl09_lnkEmail').get_attribute('href')

          # try:
          #   link =row.find_element(By.XPATH, './/tbody tr td a')
          #   print('link:', link)

          #   if link.get_attribute('id') == 'ctl09_lnkEmail' or link.get_attribute('id') == 'ctl09_lnkwebsite':
          #     if link.get_attribute('id') == 'ctl09_lnkEmail':
          #       email = self.wait_located(By.ID, 'ctl09_lnkEmail').get_attribute('href')
          #     else:
          #       website = self.wait_located(By.ID, 'ctl09_lnkwebsite').get_attribute('href')

          # except:
          #   print('error')
            # pass
    except:
      pass

    # try:
    #   email = self.wait_located(By.ID, 'ctl09_lnkEmail').get_attribute('href')
    # except:
    #   pass

    # try:
    #   website = self.wait_located(By.ID, 'ctl09_lnkwebsite').get_attribute('href')
    # except:
    #   pass

    # try:
    #   whatsapp = self.wait_located(By.ID, 'ctl09_lnktwhatsap').get_attribute('href')
    # except:
    #   pass
      
    try:
      address = self.wait_located(By.ID, 'ctl09_lblAddress').get_attribute('innerText')
    except:
      try:
        anotherData = self.wait_located(By.CSS_SELECTOR, 'table.tabrcom:nth-child(5) > tbody:nth-child(1)').get_attribute('innerText')
      except:
        pass


    if email == 'No Email' and phone == 'No Phone' and website == '':
      return []
    
    name    = self.wait_located(By.ID, 'ctl09_lblCompanyName').get_attribute('innerText')



    print(f'\nData saved: (Page: {self.pageNumber - 1} of {self.lastPageNumber}) Index: {index + 1} of {arrLen}')
    if(self.showDetails):
      print(f'\n\tName: {name} \
            \n\tPhone: {phone} \
            \n\tEmail: {email} \
            \n\tWebsite: {website} \
            \n\tAnother Data: {bool(anotherData)} \
            \n\tTime: {time.time() - startTime}'
            )

    arr = [name, address, phone, website, email, whatsapp, anotherData]

    if len(self.driver.window_handles) != 1:
      self.driver.close()
    # self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[0])
    

    return arr
  

  
  def excel_write_companydata(self, data_array : list):

    if not data_array:
      return

    for data in data_array:
      # print('wrote')
      self.spreadsheet.write(f'A{self.index}', data)
      self.index += 1
    self.index += 2







if __name__ == '__main__':
    bot = DataScrabing()
    try:
      bot.start()
    except Exception as e:
      print('Error: ', e)
      print('Something went wrong')

    print('Successfully Ended...')
