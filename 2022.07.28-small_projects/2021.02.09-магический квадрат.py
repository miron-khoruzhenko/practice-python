import random

d = []
x = []
y = []

testx = 0
testy = 0

for i in range(1,10):
    d += [i]

for i in d:
    if i % 2 == 0:
        x += [i]
    elif i % 2 and i != 5:
        y += [i]

random.shuffle(x)
random.shuffle(y)

while True:
    testx += 1

    if x[0] == 2 and x[3] != 8:
        random.shuffle(x)

    elif x[0] == 8 and x[3] != 2:
        random.shuffle(x)

    elif x[0] == 4 and x[3] != 6:
        random.shuffle(x)

    elif x[0] == 6 and x[3] != 4:
        random.shuffle(x)

    else:
        break

print('x: ' + str(testx))

while True:
    testy += 1

    if x[0] + x[1] + y[0] != 15:
        random.shuffle(y)

    elif 5 + y[1] + y[2] != 15:
        random.shuffle(y)

    elif x[2] + y[3] + x[3] != 15:
        random.shuffle(y)

    elif x[0] + y[1] + x[2] != 15:
        random.shuffle(y)

    else:
        break

print('y: ' + str(testy))

print(x[0],y[0],x[1])
print(y[1],5,y[2])
print(x[2],y[3],x[3])
