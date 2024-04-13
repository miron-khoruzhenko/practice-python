import matplotlib.pyplot as plt

x1 = [0, 100, 40]
y1 = [0, 82, 33]

# Define the points
x2 = [0, 65536, 99957]
y2 = [0, 100, 158]
# Plot the points
figure, axis = plt.subplots(1, 2) 

# axis[0].axhline(0, color='black', lw=2)

axis[0].scatter(x1, y1)
axis[1].scatter(x2, y2)

axis[0].set_xlabel('Right Volume')
axis[0].set_ylabel('Left Volume')

axis[1].set_xlabel('Volume Unit')
axis[1].set_ylabel('Volume Percent')

axis[0].set_title('Manually Defined Volume Level Graph 1')
axis[1].set_title('Percent per Unit Volume Graph 2')

# axis[0].grid()
# axis[1].grid()

axis[0].plot(x1, y1, '-')
axis[1].plot(x2, y2, '-')

for i, point in enumerate(x1):
  if i == 0:
    continue
  axis[0].annotate(f'cot: {y1[i]/x1[i]}', (x1[i], y1[i]), textcoords="offset points", xytext=(-30,0), ha='center')

for i, point in enumerate(x2):
  if i == 0:
    continue
  axis[1].annotate(f'tan: {round(x2[i]/y2[i], 3)}', (x2[i], y2[i]), textcoords="offset points", xytext=(-30,0), ha='center')


plt.show()
