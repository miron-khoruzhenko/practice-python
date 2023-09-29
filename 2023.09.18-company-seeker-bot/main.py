from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from datetime import datetime
import driverSetup
import requests
import time
import sys
import os
import re

import xlsxwriter as xl


# class DataScrabing():
class DataScrabing(driverSetup.DriverOptions):
  def __init__(self):
    super().__init__()
    
    self.excel = None 
    self.spreadsheet = None
    self.index = 1
    self.pageNumber = 1
    self.filename = f'./FindInEgypt-{self.pageNumber}-({datetime.now()}).xlsx'
    self.link = ''

    # self.test = 20


  def start(self):
    # self.excel = xl.Workbook(f'./FindInEgypt-{self.pageNumber}-{}_({datetime.now()}).xlsx')
    self.excel = xl.Workbook(self.filename)
    self.spreadsheet = self.excel.add_worksheet()


    while True:

      try:
        container = self.get_data_container()
        self.operate_foreach_of(container)
      except Exception as e:
        print('Error: ', e)
        break
    self.excel.close()




  def get_data_container(self):
    self.link = f'https://www.findinegypt.com/search?what=wood&where=&page={self.pageNumber}'
    self.driver.get(self.link)

    try:
      self.wait_clickable(By.ID, 'hs-eu-confirmation-button').click()
    except:
      pass

    dataContainer = self.driver.find_elements(By.CSS_SELECTOR, '#companies > li')
    self.pageNumber += 1

    return dataContainer



  def operate_foreach_of(self, container):
    # print('Foreach - ', end='')
    arrLen = len(container)

    for index, item in enumerate(container):
      self.excel_write_companydata(
        self.get_company_data(item, index, arrLen)
      )




  def get_company_data(self, element : WebElement, index, arrLen):
    # print('Get Company Data - ', end='')
    startTime = time.time()

    name = ''
    address = ''
    phone = ''
    website = ''
    email = ''

    try:
      phone = element.find_element(By.CSS_SELECTOR, f'.company-phone span.cursor-pointer').get_attribute('data-expanded')

    except:
      phone = 'No Phone'

    try:
        email = element.find_element(By.CSS_SELECTOR, '.company-email a').get_attribute('href')

    except Exception as e:
      # print('Mail error', e)
      email = 'No Email'


    if email == 'No Email' and phone == 'No Phone':
      return []
    

    try:
      website = element.find_element(By.CLASS_NAME, 'company-www').get_attribute('innerText')
    except:
      website = 'No Website'

    name    = element.find_element(By.TAG_NAME, 'h2').get_attribute('innerText')
    address = element.find_element(By.CLASS_NAME, 'company-address').get_attribute('innerText')

    print(f'Data saved: (Page: {self.pageNumber - 1}) Index: {index + 1} of {arrLen} \n\tName: {name} \n\tEmail: {email} \n\tPhone: {phone} \n\tWebsite: {website} \n\tTime: {time.time() - startTime}\n')
    arr = [name, address, phone, website, email]

    

    return arr
  

  
  def excel_write_companydata(self, data_array : list):
    startTime = time.time()

    if not data_array:
      return

    for data in data_array:
      # print('wrote')
      self.spreadsheet.write(f'A{self.index}', data)
      self.index += 1
    self.index += 2

    print('Excel writing: ', time.time() - startTime)







if __name__ == '__main__':
    bot = DataScrabing()
    bot.start()

    print('Successfully Ended...')
