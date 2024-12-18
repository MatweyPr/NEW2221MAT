import numpy as np

a = np.array([1.2, 2.4, 3.6, 3.5, 6.7, 1.5, 8.4, 3.1, 9.2])

#cols = len(a[0])
rows = len(a)

print('Количество строк', rows)

a.resize(9, 1)
print(a)


a.resize(3,3)
print(a)
mi = a.min(axis = 0)
mi_1 = a.min(axis = 1)
print('Минимальное число в столбце:', mi)
print('Минимальное число в строке:', mi_1)

ma = a.max(axis = 0)
ma_1 = a.max(axis = 1)
print('Максимальное число в столбце:', ma)
print('Максимальное число в строке:', ma_1)

s = a.sum(axis = 0)
s_1 = a.sum(axis = 1)
print('Сумма в столбцах:', s)
print('Сумма в строках:', s_1)