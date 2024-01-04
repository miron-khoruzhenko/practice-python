from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime, timedelta
import time

import platform

#TODO: cross-platform file systems

# if 'Windows' in platform.system():
#
#     import ctypes
#     from ctypes.wintypes import MAX_PATH
#
# dll = ctypes.windll.shell32
#         print(f'dll: {dll}')
#         buf = ctypes.create_unicode_buffer(MAX_PATH + 1)
#         print(f'buf: {buf}')
#         if dll.SHGetSpecialFolderPathW(None, buf, 0x0005, False):
#             print(buf.value)
# #prints documents folder somehow
#         else:
#             print("Failure!")

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
        with open('/home/strewen/Desktop/vscode_projects/Python/2023.03.01-lesson-bots/2023.03.01-coop-lesson-bot/account.txt') as file:
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
    except FileNotFoundError:
        print('account.txt not found')
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
    # driver.minimize_window()
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

    textbox_mail = wait.until(
        EC.presence_of_element_located((By.ID, 'Data_Mail'))
    )
    textbox_password = wait.until(
        EC.presence_of_element_located((By.ID, 'Data_Password'))
    )
    login_button = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, 'button'))
    )

    while (textbox_mail.get_property('value') != login 
        and textbox_password.get_property('value') != password):

        print('\nAttempt to login ...')
        textbox_mail.send_keys(login) 
        textbox_password.send_keys(password)

        time.sleep(0.1)

    login_button.click()

    print('Succeful login')


def openEventCalendar():
    """
    Waiting for the end of the multi-layer loader. After finishing, it goes to the event page.
    """
    print('\nLoading even calendar page...')

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

        if 'fc-not-start' in lesson.get_attribute('class'): 
            continue

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
    # FIXME: лучше возвращять так же и  прошедшие лекции
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

    for lesson in lessonData[index:]:
        if len(lesson["title"]) > 3:
            print(f'\n  {lesson["time"]}')
            print(f'  {lesson["title"][3]} -')
            print(f'  {lesson["title"][1]} {lesson["title"][2]}')

    return lessonData[:]
    # return lessonData[index:]


def waitUntil(selectedTime):
    now = datetime.now()
    #? For testing
    # now = createTimeObject("13:00")

    if selectedTime > now:
        print(f'\nSleeping until the time comes... {selectedTime.strftime("%H:%M")}')
        time.sleep((selectedTime - now).total_seconds())


def joinZoom():
    print('\nJoining to lesson...')
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[1]/div/div[7]/div/div/div/div/div/table/tbody/tr[1]/td[5]/a'))
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
    
    try:
        join_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'preview-join-button')))
    except:
        join_button = wait.until(EC.element_to_be_clickable((By.ID, 'joinBtn')))
    

    join_button.click()

    try:
        print(1)
        got_it_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div/div[2]/div/div/button[1]')))
        got_it_button.click()
        print(2)
    except:
        print('Lesson without recording')

    try:
        # time.sleep(5)
        join_with_audio = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[8]/div[3]/div/div[3]/div/button'))) 
        join_with_audio.click()
        # 
    except Exception as e:
        print(e)

    print('Zoom starting...')

def clickGotIt():
    try:
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div/div[2]/div/div/button[1]'))
        ).click()
    except:
        pass

if __name__ == '__main__':
    driver = wait = original_window = 0
    login, password = getLoginAndPassword()


    try:
        setupDriver()
        loginToSystem(login, password)
        openEventCalendar()

    except Exception as e:
        print(e)
        print('\nERROR on login')
        driver.quit()
        exit()
    
    lessons = getAvailableLessons()

    for index in range(len(lessons)):
        
        currentTime = datetime.now()
        lessonStartTime = createTimeObject(lessons[index]["startTime"])
        lessonEndTime = createTimeObject(lessons[index]["endTime"])
        #? For testing
        # currentTime = createTimeObject('13:00')

        if(lessonEndTime <= currentTime):
            continue
        
        try:
            # if(lessonStartTime - currentTime >= timedelta(minutes=10)):
            #     driver.quit()
            #     waitUntil(lessonStartTime)
            #     setupDriver()
        
            #     loginToSystem(login, password)
            #     openEventCalendar()
            #     #FIXME yeni oluşan lessons da index 2 yerine bu sefer 3 geliyor olabilir
            #     #FIXME nedeni bir dersi geçmiş olabiliyor
            #     lessons = getAvailableLessons()

            driver.quit()
            waitUntil(lessonStartTime)
            setupDriver()
    
            loginToSystem(login, password)
            openEventCalendar()
            #FIXME yeni oluşan lessons da index 2 yerine bu sefer 3 geliyor olabilir
                #FIXME nedeni bir dersi geçmiş olabiliyor
            lessons = getAvailableLessons()

            lessons[index]["linkObj"].click()
            joinZoom()
            try:
                clickGotIt()
            except: 
                pass

            waitUntil(lessonEndTime)
            # FIXME: лучше обновлять драйвер

        except Exception as e:
            print(e)
            driver.save_screenshot(f'{currentTime}-error.png')
            driver.quit()
            exit()
    
    driver.quit()
    exit()


