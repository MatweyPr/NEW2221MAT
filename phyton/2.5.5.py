import pandas as pd

df = pd.read_csv('precious_metal_new2.csv')

ma = df['gold'].max()              #максимальное в списке
print(ma)

mi = df['gold'].min()              #минимальное в списке
print(mi)

stn = (df['gold']-mi)/(ma-mi)      
print('стандартная нормализация:',stn)

sr = df['gold'].mean()             #среднее значение в столбце
print(sr)

st = df['gold'].std()              #стандартное отклонение в столбце
print(st)

mmn = (df['gold']-sr)/st
print('min-max нормализация:', mmn)
