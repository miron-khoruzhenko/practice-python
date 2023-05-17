import numpy as np

arr = np.random.random_integers(0, 15, (8, 8))
frq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for row in arr:
    for bit in row:
        frq[bit] += 1
print(frq)