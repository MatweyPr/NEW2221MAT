import pandas as pd

df = pd.read_csv('https://elteha.ru/data_science/precious_metal.csv', sep=';')
#print(df)

#new = ['gold', 'silver', 'platinum', 'palladium', 'date']
#DF = df.set_axis(new, axis = 'columns', inplace = True)
#print(DF)

DF1 = df.rename(columns ={'GOLDA':'gold', 'Silver':'silver', 'platinu':'platinum', 'Palla':'palladium', 'Date':'date'})
print(DF1)

DF2 = DF1.isnull().sum()
print(DF2)

DF3 = DF1.fillna(0)
print(DF3)