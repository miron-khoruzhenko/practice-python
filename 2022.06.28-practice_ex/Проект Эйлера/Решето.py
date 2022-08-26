def eratosthenes(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    sieve1 = [x for x in sieve if sieve[x] != 0]
    return sieve1

#*******************************************************
#Вариант 2
#*******************************************************

def eratos(n):
    a = True
    for x in range(1,n):
        for y in range(1,n):
            if x != y and y != 1:
                if not x % y:
                    a = False
                    break
        if a == True:
            print(x,end=' ')
        a = True
    
#*******************************************************
#Вариант 3
#*******************************************************

#Не ищет все числа но ищет самое большое
        
def eratos_simple(n):
    result = []
    z = 2

    while z*z <= n:
        if n%z == 0:
            result.append(z)
            z += 1
        else:
            z += 1
    return result

print(eratos_simple(600851475143))
