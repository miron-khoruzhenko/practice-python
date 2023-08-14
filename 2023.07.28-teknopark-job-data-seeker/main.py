# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import paths
import time
import textwrap

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.action_chains import ActionChains

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

        self.driver.implicitly_wait(10)
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
        building.send_keys('Kuluçka Merkezi C1 Blok') # Тестовый блок для уменьшения карточек

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
                print(prev_card_count)

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
        container = self.driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div')
        print('container: ', container)

        for item in container:
            print(item)







if __name__ == '__main__':
    bot = DataScrabing()
    bot.start()




# with open('data.txt', 'r') as file:
#     lines = file.readlines()

#     for line in lines:
#         print(line)