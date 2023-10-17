from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement

import time

class DriverOptions:
  def __init__(self):
    self.driver = 0
    self.wait = 0
    self.setup_driver()
      
  
  def setup_driver(self):
    options = Options()

    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_experimental_option("detach", True)

    # options.add_extension('./src/plugins/ablock_extension_3_19_0_0.crx')
    options.add_argument('--user-data-dir=./src/browser_profile')
    options.add_argument('--disable-gpu')
    options.add_argument("--enable-logging=stderr --v=1")

    self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)


    self.driver.implicitly_wait(.3)
    # Для работы в режиме headless
    self.driver.set_window_size(1440, 900) 


    self.wait = WebDriverWait(self.driver, .1)


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
