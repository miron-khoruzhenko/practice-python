# Python3 Program to interpolate using
# newton backward interpolation

# Calculation of u mentioned in formula
def u_cal(u, n):
	temp = u
	for i in range(n):
		temp = temp * (u + i)
	return temp

# Calculating factorial of given n
def fact(n):
	f = 1
	for i in range(2, n + 1):
		f *= i
	return f


# Driver code


# number of values given
n = 5
x = [1891, 1901, 1911, 1921, 1931]

# y is used for difference
# table and y[0] used for input
y = [[0.0 for _ in range(n)] for __ in range(n)]
y[0][0] = 46
y[1][0] = 66
y[2][0] = 81
y[3][0] = 93
y[4][0] = 101

# Calculating the backward difference table
for i in range(1, n):
	for j in range(n - 1, i - 1, -1):
		y[j][i] = y[j][i - 1] - y[j - 1][i - 1]


# Displaying the backward difference table
for i in range(n):
	for j in range(i + 1):
		print(y[i][j], end="\t")
	print()

# Value to interpolate at
value = 1925

# Initializing u and sum
sum = y[n - 1][0]
u = (value - x[n - 1]) / (x[1] - x[0])
for i in range(1, n):
	sum = sum + (u_cal(u, i) * y[n - 1][i]) / fact(i)

print("\n Value at", value, "is", sum)


# This code is contributed by phasing17
