import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets as dt

iris=dt.load_iris()         # Cargue base de datos
#print(iris.DESCR)          # Decripcion de la base de Datos
#print(iris.feature_names)  # Carcateristicas de la base de datos
#print(iris.target_names)   # Caracteriticas de las salidas        []
#print(iris.target)         # Asignacion de valores 
#print(iris.data[100])      # Un Registro o registros ([:5]) en especifico

iris_set=np.array([])

iris_set=np.stack((iris.data[0,:],iris.data[50],iris.data[100]),axis=0)   # Ingresar estacas axis( 0:Horizontal 1:Vertical )
#df_iris= pd.DataFrame(data=iris_set, index=["P0","P1","P2"], columns=["SL","SW","PL","PW"])    # Creo DataFrame

#print(iris_df.iloc[0:2])     #  Acceder a iris_df.iloc[Filas:Columnas] 
df_iris= pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)  #Lea datos de un repositiorio

X_iris=df_iris.iloc[0:150,[0,2]].values  
t = df_iris.iloc[0:150, 4].values # solo valores!

for i, j in enumerate(t):
    if t[i] == 'Iris-setosa':
        t[i] = -1
    elif t[i] == 'Iris-versicolor':
        t[i] = 0
    else:
        t[i] = 1

plt.scatter(X_iris[0:50, 0], X_iris[0:50, 1], s=175,alpha=0.6, color='blue', label='setosa')
plt.scatter(X_iris[50:100, 0], X_iris[50:100, 1], s=175,alpha=0.6, color='red', label='versicolor')
plt.scatter(X_iris[100:150, 0], X_iris[100:150, 1], s=175, alpha=0.6, color='green', label='virginica')
plt.xlabel('Longitud Sepalo')
plt.ylabel('Longitud Petalo')
plt.legend(loc='upper left')
plt.show()