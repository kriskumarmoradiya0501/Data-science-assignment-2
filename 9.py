import numpy as np


m1 = ([[125,65,75],[1,2,3]])
m2 = ([[1,6,7],[89,65,45]])

m3 = np.add(m1,m2)
m4 = np.divide(m1,m2)
m5 = np.subtract(m1,m2)

print("Matrix 1 : ",m1)
print("Matrix 2 : ",m2)
print("\n\n\nAddition : ",m3)
print("Subtraction : ",m5)
print("Division : ",m4)
   # np.linalg.inv(mtrix)