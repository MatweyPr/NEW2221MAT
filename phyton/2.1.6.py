import numpy as np
import random

a = np.array([random.randint(0, 100) for i in range(0, 100, 1)])

print('Исходный массив:', a)
k = 0
for i in a:
    if i>50:
        k +=1
print('Количество элементов > 50: ', k)

print((a>50).sum())
        
