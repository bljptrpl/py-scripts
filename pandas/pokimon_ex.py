import pandas as pd
# https://www.youtube.com/watch?v=vmEHCJofslg&ab_channel=KeithGalli

df = pd.read_csv('C:\\Users\\dvillalva\\Desktop\\scripts\pandas\\pokemon_data.csv')
#print(df.head(3))
df.to_csv('C:\\Users\\dvillalva\\Desktop\\scripts\pandas\\modified.csv', sep='\t')
# df.to_excel('modified.xlsx', index=False)
# print('test')

df['Total'] = df.iloc[:,4:10].sum(axis=1)

#print(df.head(5))

df.to_csv('C:\\Users\\dvillalva\\Desktop\\scripts\pandas\\modified.txt', index=False, sep='\t')
# df = pd.DataFrame(df)
# new_df = df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]

# Regex filtering
new_df = df.loc[~df['Name'].str.contains('Mega')]
import re 
k = df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I,regex=True)]  
print (new_df)
print(k)    
