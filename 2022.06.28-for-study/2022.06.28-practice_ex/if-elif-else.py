print("Добро пожаловать!")
name = input("Как вас зовут? ")
print("Рада знакомству,", name)
print(" ")

lvl = int(input("Введите ваш уровень доступа для продолжения "))

if lvl < 5:
    print("Sorry, you lvl is too low for this section")

elif 5 <= lvl < 10:
    print("Welcome")

else:
    print("Error")

#raw_input()
#or
input()
