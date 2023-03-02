from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime
import time

# fTODO: Когда дни пустые
# TODO: Копирование с сайта


def getTodaysLessonHours():
    dateNow = datetime.now()
    currentDay = dateNow.strftime("%A")

    def dateSort(date):
        return datetime.strptime(date, '%H:%M:%S')
    
    with open('classes.txt') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()

            # Eğer gün ya da saat yoksa
            if currentDay in line and currentDay != line:
                try:
                    lecture_hours = line.split(' ')[1:]
                    lecture_hours.sort(key=dateSort)
                    break
                except:
                    print('!!! WARNING !!!')
                    print('Incorrect time format\n')
                    print('Please write in that form:')
                    print('  Day time1 time2 ... timeN\n')
                    print('Example:')
                    print('  Monday 09:00:00 10:00:00 15:30:00\n')
                    exit()
        else:
            print('No lecture today')
            exit()

    return lecture_hours

def getLoginAndPassword():
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



def getClosestHour(hours):
    #* Şu anki saate en yakın saati buluyor ve bu saat ve sonrasını döndürüyor

    # test için
    # start_hour_string = '10:00:00'
    # now = datetime.strptime(f'{datetime.now().strftime("%d/%m/%y")} {start_hour_string}', '%d/%m/%y %H:%M:%S')
    # dateNowInMin = now.hour * 60 + now.minute
    
    dateNowInMin = datetime.now().hour * 60 + datetime.now().minute
    diff = 99999
    index = -1

    for hour in hours:
        start_time = datetime.strptime(hour, '%H:%M:%S')
        lessonHourInMin = start_time.hour * 60 + start_time.minute
        # print(f'Lesson hour {hour} in minutes - {lessonHourInMin}')
        
        if diff > abs(lessonHourInMin - dateNowInMin):
            diff = abs(lessonHourInMin - dateNowInMin)
            index = hours.index(hour)
        
    return hours[index:]



def waitUntil(start):
    now = datetime.now()

    if start > now:
        print(f'sleeping until lesson starts')
        time.sleep((start - now).total_seconds())



def loginToSystem(login, password):
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



def startLesson():
    print('\nLoading page...')
    while True:
        try:
            wait.until_not(
                EC.visibility_of_element_located((By.ID, 'loader'))
            )
            lecture_button = driver.find_element(By.CLASS_NAME, 'timeline-content')
            break
        except:
            pass

    lecture_button.click()
    print('Page loaded')
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[1]/div/div[7]/div/div/div/div/div/table/tbody/tr/td[5]/a'))
    ).click()
    print('Lesson starting...')



def joinZoom():
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
    login, password = getLoginAndPassword()

    lessonHours = getTodaysLessonHours()
    lessonHours = getClosestHour(lessonHours)

    print(f'Welcome! Today is {datetime.now().strftime("%A")}')
    print(f'Today your have {len(lessonHours)} lecture')
    print(f'In {" ".join([h[:5] for h in lessonHours])}')

    driver  = webdriver.Firefox()
    wait    = WebDriverWait(driver, 60)

    driver.implicitly_wait(10)
    driver.get('https://online.yildiz.edu.tr')
    original_window = driver.current_window_handle

    for hour in lessonHours:
        startHour = datetime.strptime(
            f'{datetime.now().strftime("%d/%m/%y")} {hour}', '%d/%m/%y %H:%M:%S')
        
        waitUntil(startHour)
        
        try:
            loginToSystem(login, password)
            startLesson()
            joinZoom()
        except Exception as e:
            print(e)
            driver.save_screenshot(f'{hour}-error.png')
            driver.quit()
            exit()
    
    driver.quit()
    exit()
