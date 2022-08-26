fib1 = 1
fib2 = 1
fibsum = 0
s = 0

while fib1 < 4000000:
    fibsum = fib1 + fib2
    fib1 = fib2
    fib2 = fibsum
    
    if fibsum % 2 == 0:
        s += fibsum

print(s)

##fib1 = fib2 = 1
## 
##n = int(input("Номер элемента ряда Фибоначчи: ")) - 2
## 
##while n > 0:
##    fib1, fib2 = fib2, fib1 + fib2
##    n -= 1
## 
##print(fib2)

##Компактный код
