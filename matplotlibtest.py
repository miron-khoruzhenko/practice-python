import scipy
import matplotlib.pyplot as plt
import numpy as np



givenData 	= [(1, 1.5), (3, 4.5), (6, 9.3), (7, 5.4), (9, 14.5)]
ys 			= []
xs 			= np.arange(1, 9, 0.1) # заполнение массива данными с интервалом в 0.1
kMatrix 	= []
kOrdinate 	= []
aList 		= []
bList 		= []



#* ==============
#* EQUATIONS

for i in range(1, len(givenData)-1):
	row = [0, 0, 0]

	if i != 1:
		print(f"({givenData[i-1][0] - givenData[i][0]}) * k[{i-1 + 1}]\t+\t", end="")
		row[i - 2] =  givenData[i-1][0] - givenData[i][0]

	else:
		print("\t0\t+\t", end="")
	
	print(f"({2 * (givenData[i-1][0] - givenData[i+1][0])}) * k[{i + 1}]",  end="")
	row[i - 1] = 2 * (givenData[i-1][0] - givenData[i+1][0])

	if i != 3:
		print(f"\t+\t({(givenData[i][0] - givenData[i+1][0])}) * k[{i+1 + 1}]",  end="")
		row[i] =  givenData[i][0] - givenData[i+1][0]
	else:
		print("\t+\t     0\t", end="")

	print(f"\t= {6 * ((givenData[i-1][1] - givenData[i][1]) / (givenData[i-1][0] - givenData[i][0]) - (givenData[i][1] - givenData[i + 1][1]) / (givenData[i][0] - givenData[i + 1][0]))}")

	kOrdinate.append(6 * ((givenData[i-1][1] - givenData[i][1]) / (givenData[i-1][0] - givenData[i][0]) - (givenData[i][1] - givenData[i + 1][1]) / (givenData[i][0] - givenData[i + 1][0])))

	kMatrix.append(row)

#* END OF EQUATIONS
#* =================



#* ==============
#* DISPLAY

kMatrix 	= np.array(kMatrix)
kOrdinate	= np.array(kOrdinate)

print("\n\nMatrix of k:\n",kMatrix)
print("\nOrdinade of k:\n",kOrdinate)

matrixSolution = np.linalg.solve(kMatrix, kOrdinate)
matrixSolution = np.insert(matrixSolution, 0, 0)
matrixSolution = np.append(matrixSolution, 0)

print("\nMatrix solution:")
for i in range(len(matrixSolution)):
	print(f"k[{i+1}] = ", matrixSolution[i])

#* END OF DISPLAY
#* ==============



#* =======================
#* A AND B LIST GENERATION

for i in range(len(givenData) - 1):
	aList.append(givenData[i][1] / (givenData[i][0] - givenData[i+1][0]) - 1/6 * matrixSolution[i] * (givenData[i][0] - givenData[i+1][0]))
	bList.append(givenData[i+1][1]/(givenData[i][0] - givenData[i+1][0]) - 1/6 * matrixSolution[i+1] * (givenData[i][0] - givenData[i + 1][0]))

aList = np.array(aList)
bList = np.array(bList)

print("\nAll A array elements: ",aList)
print("All B array elements: ",bList)

#* A AND B LIST GENERATION
#* =======================



#* =====================
#* CUBIC INTERPOLATION

plot = np.array([])
for i in range(len(givenData)-1):
	if i != len(givenData) - 1:
		for x in np.arange(givenData[i][0], givenData[i + 1][0], 0.1):
			plot = np.append(plot, (
				(matrixSolution[i] * ((x - givenData[i+1][0]) ** 3) - matrixSolution[i+1] * ((x - givenData[i][0]) ** 3)) 
				/
				(6 * (givenData[i][0] - givenData[i+1][0])) + aList[i] * (x - givenData[i+1][0]) - bList[i] * (x - givenData[i][0]))
				)
	else:
		x = 9.01
		plot = np.append(plot, (
			(matrixSolution[i] * ((x - givenData[i+1][0]) ** 3) - matrixSolution[i+1] * ((x - givenData[i][0]) ** 3)) 
			/
			(6 * (givenData[i][0] - givenData[i+1][0])) + aList[i] * (x - givenData[i+1][0]) - bList[i] * (x - givenData[i][0]))
			)

print("\nOur cubic interpolation:\n",plot)
#* END OF CUBIC INTERPOLATION
#* =====================



#* ===========
#* PLOT DRAW

plt.plot(xs, plot, label="S")

plt.xticks(np.arange(min(xs), max(xs) + 1, 0.5))
plt.yticks(np.arange(min(plot), max(plot) + 1, 0.75))

plt.ylabel('y')
plt.xlabel('x')

plt.grid(True, axis='both', color="#dddddd", linestyle='-.')
plt.legend(loc='lower right', ncol=2)

plt.show()

#* END
#* ===========

