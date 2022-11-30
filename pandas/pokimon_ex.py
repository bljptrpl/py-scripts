import pandas as pd
# https://www.youtube.com/watch?v=vmEHCJofslg&ab_channel=KeithGalli

df = pd.read_csv('C:\\Users\\dvillalva\\Desktop\\scripts\pandas\\pokemon_data.csv')
#print(df.head(3))
df.to_csv('C:\\Users\\dvillalva\\Desktop\\scripts\pandas\\modified.csv', sep='\t')
# df.to_excel('modified.xlsx', index=False)
# print('test')

df['Total'] = df.iloc[:,4:10].sum(axis=1)

print(df.head(5))