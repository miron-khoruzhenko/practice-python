##Простые делители числа 13195 - это 5, 7, 13 и 29.
##
##Каков самый большой делитель числа 600851475143,
##являющийся простым числом?

n = int(input())
startInt = 2
intlist = range(2, n+1)

while startInt**2 < max(intlist):
    for i in intlist:
        startInt += 1
        print (startInt)
