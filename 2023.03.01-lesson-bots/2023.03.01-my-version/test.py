from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
import time

#TODO: Eğer account file yoksa yaratsın ve console'a o file'a password ve login girmseini istesin
#TODO: kalan fonklarin descr yazmak

def getLoginAndPassword():
    """ opens account.txt and searches for strings containing 
    Password and Login takes the value following them and returns 
    as a pair login, password
    """
    login = ''
    password = ''

    try:
        with open('account.txt') as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()

                if 'Login:' in line and "Login:" != line:
                    try:
                        login = line.split(' ')[1]
                        break
                    except:
                        print('Something went wrong. Please control your date file and login.')
            else:
                print('Please enter login')
                exit()

            for line in lines:
                line = line.strip()

                if 'Password:' in line and "Password:" != line:
                    try:
                        password = line.split(' ')[1]
                        break
                    except:
                        print('Something went wrong. Please control your date file and password.')
            else:
                print('Please enter password')
                exit()
    except:
        print('ERROR: Control your path and cwd (working directory)')
        exit()

    return (login, password)


def createTimeObject(hour):
    return datetime.strptime(
        f'{datetime.now().strftime("%d/%m/%y")} {hour}', '%d/%m/%y %H:%M'
    )


def setupDriver():
    print('Connetcting driver...')
    global driver, wait, original_window

    driver  = webdriver.Firefox()
    wait    = WebDriverWait(driver, 60)

    driver.implicitly_wait(10)
    driver.get('https://online.yildiz.edu.tr')
    original_window = driver.current_window_handle
    
    if driver != 0:
        print('Driver succesfully connected!')


def loginToSystem(login, password):
    """Finds the login and password field and enters 
    the login and password passed to this function there. 
    Then he presses the login button.
    """
    print('\nAttempt to login ...')

    textbox_mail = wait.until(
        EC.presence_of_element_located((By.ID, 'Data_Mail'))
    )
    textbox_password = wait.until(
        EC.presence_of_element_located((By.ID, 'Data_Password'))
    )
    login_button = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, 'button'))
    )
    textbox_mail.send_keys(login) 
    textbox_password.send_keys(password)
    login_button.click()
    
    print('Succeful login')


def openEventCalendar():
    """
    Waiting for the end of the multi-layer loader. After finishing, it goes to the event page.
    """
    print('\nLoading page...')

    while True:
        try:
            wait.until_not(
                EC.visibility_of_element_located((By.ID, 'loader'))
            )
            event_calendar = driver.find_element(
                By.XPATH, '/html/body/main/div/div[1]/div/div[7]/div/div/div/div[2]/ul/li[3]/a')
            break
        except:
            pass

    event_calendar.click()
    print('Event calendar page loaded')


def getLessonsData():
    lessonData = []
    
    #* Bütün günleri tutan parent
    thead_parent = driver.find_elements(
                By.XPATH, '/html/body/main/div/div[1]/div/div[7]/div/div/div/div[2]/div/div[3]/div/div[2]/div/table/thead/tr/td/div/table/thead/tr/th')


    #* Bizim gübü temsil eden th ve onun indexi
    index = 0
    for th in thead_parent:
        # print(th.get_attribute("class"))fc-thu

        #? For testing
        # if('fc-thu' in th.get_attribute('class')):
        if('fc-today' in th.get_attribute('class')):
            break
        index += 1
    

    #* th ile aynı satırdaki td'nın linkleri. Bu linkler bizim derseri temsil ederler
    try:
        allLessons = driver.find_elements(
            By.XPATH, f'/html/body/main/div/div[1]/div/div[7]/div/div/div/div[2]/div/div[3]/div/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[{index + 1}]/div/div[2]/a'
        )
        # print(allLessons)
    except:
        print('No lecture today')
        driver.quit()
        exit()

    index = 0
    for lesson in allLessons:

        lessonTime      = lesson.find_element(By.CLASS_NAME, 'fc-time')
        lessonStartTime = lessonTime.get_attribute('data-start')
        lessonEndTime   = lessonTime.get_attribute('data-full')[8:]
        lessonTitle     = lesson.find_element(By.CLASS_NAME, 'fc-title')

        lessonData.append({
            "index" : index,

            "linkObj"   : lesson,
            "startTime" : lessonStartTime,
            "endTime"   : lessonEndTime,

            "time"  : lessonTime.text,
            "title" : lessonTitle.text.split('\n'),
        })

        index += 1
    
    return lessonData


def getAvailableLessons():
    print("\nGet available lessons...")
    lessonData = getLessonsData()

    if len(lessonData) == 0:
        print('No lecture today...')
        driver.quit()
        exit()

    currentTime = datetime.now()

    index = 0

    for lesson in lessonData:
        lessonEndTime = createTimeObject(lesson["endTime"])

        if currentTime > lessonEndTime:
            index += 1
        else:
            break
    
    print('Available lessons:')

    for lesson in lessonData[1:]:
        print(f'\n  {lesson["time"]}')
        print(f'  {lesson["title"][3]} -')
        print(f'  {lesson["title"][1]} {lesson["title"][2]}')

    return lessonData[1:]


def waitUntil(selectedTime):
    now = datetime.now()

    if selectedTime > now:
        print(f'\nSleeping until the time comes...')
        time.sleep((selectedTime - now).total_seconds())


def joinZoom():
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[1]/div/div[7]/div/div/div/div/div/table/tbody/tr/td[5]/a'))
    ).click()

    print('\nWaiting for zoom...')
    wait.until(EC.number_of_windows_to_be(2))

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    wait.until(EC.title_contains('Zoom'))

    current_url = driver.current_url
    new_url = current_url.replace('w/', 'wc/join/')
    driver.get(new_url)
    join_button = wait.until(EC.element_to_be_clickable((By.ID, 'joinBtn')))

    join_button.click()
    print('Zoom starting...')



if __name__ == '__main__':
    driver = wait = original_window = 0
    login, password = getLoginAndPassword()
    setupDriver()

    try:
        loginToSystem(login, password)
        openEventCalendar()

    except Exception as e:
        print(e)
        print('\nERROR on login')
        driver.quit()
        exit()
    
    lessons = getAvailableLessons()


    for lesson in lessons:
        driver.quit()

        currentTime = datetime.now()
        lessonStartTime = createTimeObject(lesson["startTime"])
        lessonEndTime = createTimeObject(lesson["endTime"])

        waitUntil(lessonStartTime)
        setupDriver()
        
        try:
            loginToSystem(login, password)
            openEventCalendar()

            lesson["linkObj"].click()
            joinZoom()

            waitUntil(lessonEndTime)

        except Exception as e:
            print(e)
            driver.save_screenshot(f'{currentTime}-error.png')
            driver.quit()
            exit()
    
    driver.quit()
    exit()