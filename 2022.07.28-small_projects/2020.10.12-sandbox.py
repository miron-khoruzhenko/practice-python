x = ['aja 1', 'aja 2', 'fdfs', 'aja 4', 'sadfdfs']
y = []

for i in range(len(x)):
    if 'aja' in x[i]:
        y.append(x[i][4:])
    else:
        y.append(x[i])
