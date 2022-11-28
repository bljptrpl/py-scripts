import pandas as pd

df = pd.read_csv('C:\\Users\\dvillalva\\Desktop\\scripts\pandas\\pokemon_data.csv')
print(df.head(3))
df.to_csv('C:\\Users\\dvillalva\\Desktop\\scripts\pandas\\modified.csv', sep='\t')
# df.to_excel('modified.xlsx', index=False)
print('test')

