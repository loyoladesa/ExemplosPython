import pandas as pd

data = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(data,columns=[0,1,2])

print('df Original')
print(df)

def add_numbers(x):
    return f'{x}01'

df[0] = df[0].apply(add_numbers)

print('df Modificado')
print(df)

df[1]=df[1].apply(lambda x:f'{x}01')

print('df Modificado com Lambda')
print(df)