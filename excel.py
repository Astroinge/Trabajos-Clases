import pandas as pd 
df=pd.read_excel("pruebaexcel.xlsx")
print(df)
media=df['prueba'].mean()
print(media)
mediana=df['prueba'].median()
print(mediana)
varianza=df['prueba'].var()
print(varianza)

