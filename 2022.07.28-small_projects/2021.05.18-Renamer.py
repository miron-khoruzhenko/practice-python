import os


#####################################################
##################### Фунцкции ######################
#####################################################

clear = lambda: os.system('cls')

def isToDo():
    return False if toDo in ['c', 'a', 'r', 'rename', 'cut', 'add'] else True

def wall():
    print("######################################################################")
    print("x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x  x")
    print("######################################################################\n")

def getPath():
    global folder
    
    print('if you want to enter full path, write FULLPATH')
    folder = input("Enter folder name on your desktop: ")

    if folder.upper() == "FULLPATH":
        accept = 0
        while not accept:
            path = input("Enter full path: ")
            #print(path)

            while True:
                print("confirm? Y / N")
                accept = input()
                if accept.upper() == "Y":
                    accept = True
                    break
                elif accept.upper() == "N":
                    accept = False
                    break
                else:
                    print("Please enter only Y or N")
    else:
        path = 'C:\\Users\\Strewen\\Desktop\\' + folder
    #из за того что в юникоде \u означает \U00014321 это создает ошибку.
    #что бы избежать такой ошибки нужно удвоить обратные слэши или написать ...
    # r'C:\Users\Strewen\Desktop\123'

    return path

#####################################################
#################### Программма #####################
#####################################################

folder = None
toDo = None
changeThis = None
count = None
newNames = []

#*Проверка на правильность пути
while True:
    path = getPath()
    try:
        files = os.listdir(path)
        clear()
        break
    except:
        print("\n#####################################################################")
        print("x  x  x  x  x  x  x  x  x  !  Wrong Way  !  x  x  x  x  x  x  x  x  x")
        print("#####################################################################\n")

wall()
print("""Please enter accurately and comma separated.
For example you can delete "test" and "test2" segments in 
"test somename.txt" and "test2 another.mp3" files by select "Delete" 
and type "test ,test2 " (don't forget spaces)
if you want to delete "y2mate.com - " just write "y2"

In the same way if you want to replace "segment1" in 
"segment1 file.txt" to "segment2" just select "Replace" and
write the segment to replace first and what to replace after

And if you want ot add something at the beginning, 
just select "Add" and enter segment you want to add\n""")

#*Проверка на правильность выбора функции
while isToDo():
    wall()
    toDo =  input("""Do you want to cut, rename or add a segment?
    Cut(c)/Rename(r)/Add(a): """).lower()
    clear()



################################################################
######################## Основной цикл #########################
################################################################

#вырезать сегмент
if toDo == 'c':
    wall()
    changeThis = input("The segments you want to delete: ")
    
    if changeThis == 'y2':
        changeThis = 'y2mate.com - '

        for i in range(len(files)):
            if changeThis in files[i]:
                newNames.append(files[i][len(changeThis):])
            else:
                #так как слово для изменения всего одно, это не нарушает структуру
                newNames.append(files[i])

    else:
        changeThisThings = changeThis.split(',')
        for i in files:
            newNames.append(i)

        for j in range(len(changeThisThings)):
            for i in range(len(files)):
                if changeThisThings[j] in files[i]:
                    #newNames.append(files[i][len(deleteThisThings[j]):])
                    newNames[i] = files[i][len(changeThisThings[j]):]

                else:
                    #тут слов для изменения больше из за чего else используется чаще.
                    continue

#заменить сегмент на другой
elif toDo == 'r':
    wall()
    changingSegment = input("The segment you want to replace: ")
    changeToThis = input("Replace with: ")

    for i in files:
        newNames.append(i)

    for i in range(len(files)):
        if changingSegment in files[i]:
            newNames[i] = files[i].replace(changingSegment, changeToThis)

        else:
            continue

#добавить сегмент в начало фаила
else:
    wall()
    addThis = input("Enter what you want to add at the beginning: ")
    
    for i in files:
        newNames.append(i)

    for i in range(len(files)):
        #newNames.append(files[i][len(deleteThisThings[j]):])
        newNames[i] = addThis + " " + files[i]

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
#################### Конец основного цикла #####################
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#

clear()
os.chdir(path)

wall()

for i in range(len(files)):
    try:
        os.rename(files[i], newNames[i])
        if files[i] != newNames[i]: 
            print(files[i] + "\t--->\t" + newNames[i])
            count = 1
        

    except:
        os.remove(path+"\\"+files[i])
        print("(!)Deleted:\t"+files[i])

    #если это последняя итерация и была хоть одна замена фаила
    if i == len(files)-1 and count==1:
        print("") 
print("\t\t\t   Successful\n")
wall()
input()
