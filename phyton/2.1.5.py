import numpy as np

A = np.array([[2,8], [1,-6]])
B = np.array([[3,2,7],[4,1,8],[6,3,7]])
C = np.array([[4,3,2,7], [6,1,1,-2], [7,5,8,1],[9,5,-3,-5]])

Tr_A = A.transpose()
Tr_B = B.transpose()
Tr_C = C.transpose()

print('Транспонированные матрицы:')
print(Tr_A)
print(Tr_B)
print(Tr_C)

Ob_A = np.linalg.inv(A)
Ob_B = np.linalg.inv(B)
Ob_C = np.linalg.inv(C)

print('Обратные матрицы:')
print(Ob_A)
print(Ob_B)
print(Ob_C)

Op_A = np.linalg.det(A)
Op_B = np.linalg.det(B)
Op_C = np.linalg.det(C)

print('Определитель матриц:')
print(Op_A)
print(Op_B)
print(Op_C)

N_B = np.linalg.norm(B,3,axis=1)

print('Норма векторов из строк матрицы 3x3:')
print(N_B)

N_C = np.linalg.norm(C,4,axis=0)

print('Норма векторов из столбцов матрицы 4x4:')
print(N_C)
