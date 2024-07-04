import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
from tensorflow import keras
from keras import models
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import read_excel
import tensorflow as tf

## Cargar Modelo Json
json_file = open('model_03.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = keras.models.model_from_json(loaded_model_json)

# Cargar Pesos
loaded_model.load_weights("model_03.weights.h5")
print("Modelo Cargado")

# Cargar Datos
df1 = pd.read_excel('data_1.xlsx')

# Matriz 1171 x 2
colums=["Entrada","Salida"]
rows=300

# Vector de Salida (Out)
out_colum = 'yk'
target_data = df1[out_colum].iloc[:rows].values
target_data = np.asarray(target_data).astype('float32')

# U(k)
input_Columns ="uk"
uk= df1[input_Columns].iloc[:rows].values
uk = np.asarray(uk).astype('float32')
 
# Inicializacion de vectores para verificacion de la red
yk  =[]
uk_1=[0]
uk_2=[0]
yk_1=[0]
yk_2=[0]

aux_uk_1=0
aux_uk_2=0
aux_yk_1=0
aux_yk_2=0

## Verificacion de la red 
for i in range(1 ,len(uk),1):
    yk.append(float(loaded_model.predict([[aux_uk_1,aux_uk_2,aux_yk_1,aux_yk_2]])))
    aux_yk_1=float(yk[-1])
    yk_1.append(aux_yk_1)
    aux_yk_2=float(yk_1[-1])
    yk_2.append(aux_yk_2)
    aux_uk_1 = float(uk[i])
    aux_uk_2 = float(uk[i-1])
    print(i)

plt.grid()
plt.title('Verificacion Modelo')
plt.plot(uk,'b-',linewidth=3)
plt.plot(yk,'r-',linewidth=2)
plt.legend(['U(k)','Y(K)','Y_(K)' ],loc = "upper right")
plt.ylabel(' Y(K)',fontsize=14)
plt.xlabel('Time (s)',fontsize=14)
plt.show()

