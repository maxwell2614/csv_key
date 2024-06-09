import pandas as pd
df=pd.read_excel('лица.xlsx')

idx=2
new_col = 'NAN'
df.insert(loc=idx, column='key', value=new_col)

df['BIRTH_DAY']=df['BIRTH_DAY'].astype(str)
df['BIRTH_MONTH']=df['BIRTH_MONTH'].astype(str)
df['BIRTH_YEAR']=df['BIRTH_YEAR'].astype(str)

df['key'] = df.PATRONYMIC_NAME_CYR.str[:3]+df.FIRST_NAME_CYR.str[:3]+df.BIRTH_DAY+df.BIRTH_MONTH+df.BIRTH_YEAR


df1=pd.read_excel('Неразрешения.xlsx')
df1.insert(loc=idx,column='key', value=new_col)

df1['BIRTH_DAY']=df1['BIRTH_DAY'].astype(str)
df1['BIRTH_MONTH']=df1['BIRTH_MONTH'].astype(str)
df1['BIRTH_YEAR']=df1['BIRTH_YEAR'].astype(str)

df1['key'] = df1.PATRONYMIC_NAME_CYR.str[:3]+df1.FIRST_NAME_CYR.str[:3]+df1.BIRTH_DAY+df1.BIRTH_MONTH+df1.BIRTH_YEAR

# pd.merge(df, df1, on='key', how='left')

print(df1)