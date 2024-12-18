import numpy as np

M = np.array([[5, 4], [2, -6]])  #Матрица
V = np.array([14, -2])             #Вектор

O = np.linalg.solve(M,V)
print(O)