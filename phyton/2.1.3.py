import numpy as np

a = np.array([[4,2], [9,1]])
b = np.array([[5,3], [2,5]])

M = np.row_stack([a,b])
print('Массив из 4-х строк и 2-х столбцов:')
print(M)

Sr = M[0:3, :]
print('Срез:')
print(Sr)

print('Сумма элементов:',Sr.sum())
print('Максимальный элемент:',Sr.max())
print('Минимальный элемент:',Sr.min())

N = np.column_stack([a,b])
print('Массив из 2-х строк и 4-х столбцов:')
print(N)

Sr_1 = N[:1, 0:3]
print('Срез:')
print(Sr_1)
print('Сумма элементов:',Sr_1.sum())
print('Максимальный элемент:',Sr_1.max())
print('Минимальный элемент:',Sr_1.min())