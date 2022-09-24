while True:
    num = input("Number: ")

    for i in num:
        if i.isdigit() == False:
            num = 0
    if num == 0:
        continue
    break

def Luhn():
    total = 0
    for i in num[-2::-2]:
        if int(i)*2 >= 10:
            i = str(int(i)*2)
            i = int(i[0]) + int(i[1])
            total += i
            continue
        i = int(i)*2
        total += int(i)
    for i in num[::-2]:
        total += int(i)
    return 0 == total%10

if int(num[0:2]) in [34, 37] and Luhn() and len(num) == 15:
    print("AMEX")

elif int(num[0:2]) in [51, 52, 53, 54, 55] and Luhn() and len(num) == 16:
    print("MASTERCARD")

elif int(num[0:1]) == 4 and Luhn() and len(num) in [13, 16]:
    print("VISA")

else:
    print("INVALID")
