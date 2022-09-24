allData = {
'Gmail':{'outbigchat@gmail.com':'parolotspampochti',
        'tranquil.mist.jonquil@gmail.com':'parolotpantovoypochti',
        'zauredastan@gmail.com':'135531Miron',
        'guestguest1219@gmail.com':'qsczseqsczse',
        'mironkhoruzhenko@gmail.com':'parolotlichnoypochtigmail',
        'miron1000000@gmail.com':'parolotosnovnoypochti'},

'Mojang':{'miron1000000@gmail.com':'Xt2SDC3pvs9Q'},

'VK':{'ourbigchat@gmail.com':'ourbigchat@gmail.com'},

'Hotmail':{'ourbigchat@gmail.com':'parolotspampochtihotmail8',
            'miron1000000@gmail.com':'20010802m',
            'l6a20926@std.yildiz.edu.tr':'xtw5lp}bR2qwdY%'},

'İnstagram':{'mironkhoruzhenko (ourbigchat@gmail.com)':'nadezhnyiparolotinstagram',
            'miron.kh_ (guestguest1219@gmail.com)':'updated20010802m'},

'USIS':{'l6A20926':'e977rxha'},

'moodleybd':{'miron':'20010802Miron!'}
}

while True:
    print("list - Для вывода списка")
    print("reg - для сохранения нового элемента")
    print("del - для удаления нового элемемнта")

    userInput = input()

    if userInput == "list":
        x = 0
        listCount = 0
        for k in allData.keys():
            listCount+= 1
            print(str(listCount) + '. ' + k)
        while True:
            listCount = 0;
            x = input('\n Выберите желаемый список\n')
            if x.isalpha() and x in allData.keys():
                break
            else:

                print('Повторите попытку')

        for k, v in allData[x].items():
            print(k + ' : ' + v)

        break

    elif userInput == "reg":
        break

    elif userInput == "del":
        break

    else:
        print("Error please try again");
input()
