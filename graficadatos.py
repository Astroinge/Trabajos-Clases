import pandas as pd  
import matplotlib.pyplot as plt 
df=pd.read_csv('datosgrafica.csv')
fig,ax=plt.subplots()
ax.scatter(['x_datosgrafica'],['y_datosgrafica'])
plt.show()