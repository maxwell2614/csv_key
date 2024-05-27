import pandas as pd
df=pd.read_csv("2.csv")

df["key"]=(["first_name"])[0:2]

print(df)
