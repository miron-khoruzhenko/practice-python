import os
import datetime


path = os.path.abspath(os.getcwd())
# files = os.listdir(path)

os.system('color 06')

files = os.listdir()
mp3_list = []
edited_count = 0

today = datetime.datetime.now()

for file in files:
    if file.endswith('.mp3'):
        mp3_list.append(file)

if len(mp3_list) > 0:
    filename = "{}.{}.{}-musicLog.txt".format(today.year, today.month, today.day)
    txt = open(filename, 'a', encoding="utf-8")

    for file in mp3_list:
        old_file = file
        i = file.find(']')

        if file[i-8 : i] == ' - Topic':
            file = file[:i-8] + file[i:]

        elif file[1 : i] == file[i+2 : i*2+1]:
            file = file[:i+1] + file[i*2+1:]

        if old_file != file:

            try:
                os.rename(old_file, file)

                edited_count += 1
                print('Edited: ', end='')
                print(old_file)
            
            except Exception as e:
                if e.args[0] != 17:
                    print(e)
                    break
                continue

        
        txt.write(file + '\n')

    txt.close()

    b = input('Successful')

else:
    print('Nothing happpen...')
    b = input()