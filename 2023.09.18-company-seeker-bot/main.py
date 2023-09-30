from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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
    self.lastPageNumber = 13
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
    if(self.lastPageNumber and self.pageNumber > self.lastPageNumber):
      raise Exception('Last Page Finished')
    
    # self.link = f'https://www.findinegypt.com/search?what=wood&where=&page={self.pageNumber}'
    # self.link = f'https://www.findinegypt.com/search?what=&category=cement-concrete-gypsum-brick-equipment&page={self.pageNumber}'
    # self.link = f'https://www.findinegypt.com/search?what=metal&where='
    self.link = f'https://www.findinegypt.com/search?what=&category=insulation'

    self.driver.get(self.link + f'&page={self.pageNumber}')

    # try:
    #   self.wait_clickable(By.ID, 'hs-eu-confirmation-button').click()
    # except:
    #   pass

    dataContainer = self.driver.find_elements(By.CSS_SELECTOR, '.line-company')
    self.pageNumber += 1

    return dataContainer



  def operate_foreach_of(self, container):
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
      link = element.find_element(By.TAG_NAME, 'a')
      link.send_keys(Keys.CONTROL + Keys.RETURN)

      self.driver.switch_to.window(self.driver.window_handles[-1])

    except:
      return

    try:
      phone = self.wait_located(By.CSS_SELECTOR, f'.single-company-phone').get_attribute('innerText')

    except:
      phone = 'No Phone'


    if email == 'No Email' and phone == 'No Phone':
      return []
    
    name    = self.wait_located(By.CLASS_NAME, 'single-company-name').get_attribute('innerText')
    address = self.wait_located(By.CLASS_NAME, 'single-company-adress').get_attribute('innerText')

    print(f'Data saved: (Page: {self.pageNumber - 1}) Index: {index + 1} of {arrLen} \n\tName: {name} \n\tEmail: {email} \n\tPhone: {phone} \n\tWebsite: {website} \n\tTime: {time.time() - startTime}\n')
    arr = [name, address, phone, website, email]

    self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[0])
    

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
