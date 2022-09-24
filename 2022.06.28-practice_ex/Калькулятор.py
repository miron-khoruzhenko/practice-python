print('Внимание, напишите "q" что бы выйти из программы')
print()

while 1:
    print("Выберите функци: +, -, *, / ")
    a=input()
    
    if a in ('+','-','*','/'):
        x=float(input('Первое число: '))
        y=float(input('Второе число: '))

        if a == '+':
            print(x+y)
        elif a == '-':
            print(x-y)
        elif a == '*':
            print(x*y)
        else:
            print(x/y)
        
    elif a == 'q':
        break

    else:
        print('Вы ввели неправильный символ. Пожалуйста повторите')
        print()
    
