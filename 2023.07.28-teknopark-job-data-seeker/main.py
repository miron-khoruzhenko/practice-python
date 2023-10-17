# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import paths
import time
import textwrap

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains
import sys




class DriverOptions:
    def __init__(self):
        self.driver = 0
        self.wait = 0
        self.setup_driver()
        
    
    def setup_driver(self):
        # options = FirefoxOptions()
        options = Options()

        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        # options.add_experimental_option("detach", True)


        # self.driver = Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()), options=options)
        self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

        self.driver.implicitly_wait(5)
        # Для работы в режиме headless
        self.driver.set_window_size(1440, 900) 


        self.wait = WebDriverWait(self.driver, 10)
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

class DataScrabing(DriverOptions):
    def __init__(self):
        super().__init__()
        self.dynamic_word_len = 0


    def start(self):
        self.driver.get(paths.company_list_url)
        
        self.set_advanced_search()


    def set_advanced_search(self):
        '''
        Задает настройки для улучшеного поиска. 
        '''
        adv_btn = self.wait_clickable(By.XPATH, paths.adv_search_btn)
        adv_btn.click()

        sector = self.wait_located(By.ID, paths.sector_ID)
        location = self.wait_located(By.ID, paths.location_ID)
        building = self.wait_located(By.ID, paths.building_ID)

        # Заполнение формы для поиска
        sector.send_keys('Yazılım')
        location.send_keys('YTÜ YILDIZ TEKNOPARK DAVUTPAŞA YERLEŞKESİ')
        # building.send_keys('Kuluçka Merkezi C1 Blok') # Тестовый блок для уменьшения карточyек

        search_btn = self.wait_clickable(By.XPATH, paths.search_btn)

        while True:
            try:
                search_btn.click()
                print('The search was started successfully ')
                break
            except:
                print('The search failed. Retry...')
                time.sleep(1)
        
        self.show_all_cards()
        self.process_container_with()

    def dynamic_print(self, dynamic_msg):
        write = sys.stdout.write
        write('\b' * self.dynamic_word_len)

        write(dynamic_msg + ' ' * 5)
        # write(f'{self.dynamic_word_len}')
                
        self.dynamic_word_len = len(dynamic_msg) + 1 + 5
    
        # write('\n')



    def get_cards_count(self):
        cards = self.driver.find_elements(By.XPATH, paths.company_cards)

        return len(cards)
        
    def show_all_cards(self):
        start_time = time.time()
        click_count = 0
        prev_card_count = 0
        load_more_btn = self.wait_clickable(By.XPATH, paths.load_more_btn)
        print("Loading .", end=' ')

        while True:
            print('.', end=' ')

            try:                
                load_more_btn.click()

                # Жду подгрузку
                while prev_card_count == self.get_cards_count():
                    time.sleep(.3)

                prev_card_count = self.get_cards_count()

            except: 
                try:
                    self.wait_clickable(By.XPATH, paths.load_more_btn)
                except:
                    break
                    
            click_count += 1

        print(textwrap.dedent(f'''\n\n
            ========================================

            The search was completed successfully

            Total Clicks   : {click_count}
            Card Count     : {prev_card_count}
            Run Time       : {time.time() - start_time}

            ========================================

            '''))
        
    # def process_container_with(self, functions=print):
    def process_container_with(self):
        container = self.driver.find_elements(By.XPATH, paths.company_cards)
        companies_wroted = 0

        self.driver.execute_script('console.log("hello")')
        file = open('text.md', 'w')
        

        for index, item in enumerate(container):
            link = item.find_element(By.XPATH, './/div/div/a')
            # heading = item.find_element(By.XPATH, './/div/div/a/h6')

            # print(heading.get_attribute('innerText'))
            # file.write(heading.get_attribute('innerText') + '\n')

            link.send_keys(Keys.CONTROL + Keys.RETURN)
            self.driver.switch_to.window(self.driver.window_handles[-1])

            descr = self.wait_located(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[1]/table/tbody')
            file.write(descr.find_element(By.XPATH, './/tr[2]').get_attribute('innerText') + '\n')
            file.write(descr.find_element(By.XPATH, './/tr[4]').get_attribute('innerText') + '\n')
            file.write(descr.find_element(By.XPATH, './/tr[5]').get_attribute('innerText') + '\n')
            file.write(descr.find_element(By.XPATH, './/tr[6]').get_attribute('innerText').replace('http://', '') + '\n')
            file.write('\n')
            # file.write(descr.get_attribute('innerText') + '\n\n')

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            companies_wroted += 1

            self.dynamic_print(f'Companies Saved: {companies_wroted}')
        print()







if __name__ == '__main__':
    bot = DataScrabing()
    bot.start()
