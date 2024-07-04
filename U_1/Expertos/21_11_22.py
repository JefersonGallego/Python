import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from perceptron_LMS import*

df_iris= pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None) 

iris_set = df_iris[df_iris.iloc[:, 4] == 'Iris-setosa']     #Considere todas las filas 
iris_ver = df_iris[df_iris.iloc[:, 4] == 'Iris-versicolor']
iris_sv = pd.concat([iris_set, iris_ver], axis=0)
x_train, x_test, y_train, y_test =train_test_split(iris_sv.iloc[:, [0,2]], iris_sv.iloc[:,4]) # Entrenamiento y Verificacion  [0,2]] = Solo Fila Cero y la Dos

y_tr = np.array([])  
setosa = 0
versicolor = 0

for i, j in enumerate(y_train):
    if y_train.iloc[i] == 'Iris-setosa':
        y_tr = np.append(y_tr, -1)
        setosa += 1
    else:
        y_tr = np.append(y_tr, 1)
        versicolor += 1
        
x_tr = np.stack((np.ones(len(x_train)), x_train.iloc[:,0],x_train.iloc[:,1]),axis = 1)   # Stack = Coloque estacas  np.ones= Llene de 1  axis= 1:V 0:H
w = algoritmo_LMS(x_tr, y_tr, alfa=0.15, epochs=5)
y_tt = np.array([])

for j, k in enumerate(y_test):
    if y_test.iloc[j] == 'Iris-setosa':
        y_tt = np.append(y_tt, -1)
    else:
        y_tt = np.append(y_tt, 1)


X_tt = np.stack((np.ones(len(x_test)), x_test.iloc[:,0],x_test.iloc[:,1]), axis=1)

clases = percep_out(X_tt, w)

print(clases==y_tt)

bound_reg(X_tt,clases,w)