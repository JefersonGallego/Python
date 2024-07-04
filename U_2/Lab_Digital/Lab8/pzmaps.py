# -*- coding: utf-8 -*-
"""
Funciones de transferencia

Pedro Alejandro Sanchez Osorio
Victor Alfonso Moyano Echeverri
Jeferson Gallego Chaverra

"""
import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *

# Mapa se Zeros y Polos

# Modifica el tamaño de los ejes
plt.rcParams.update({'font.size':10})

#Kp: 2.2472328285247647
#taup: 213.16858982908337
#thetap: 9.621762010893972

# Tclab
Ts=15
# Continuo
numc=[2.247]
denc=[213.168,1,]
# Discreto
numd=[0.056175,0.096621]
dend=[1,-0.9321,0]

# FT 
Gs = tf(numc,denc)
Gz_2=tf(numd,dend,Ts)

print(Gs)
print(Gz_2)


#%% Mapa de Polos y Ceros
#plt.figure(1)
pzmap(Gs,grid=True)    
plt.figure(2)  
pzmap(Gz_2,grid=True)
plt.grid()

print("Polos Continuos")
for i , p in enumerate(pole(Gs)):
    print(f"Polo {i+1}: {p:.4}")

print("Zeros Continuos")

for i , z in enumerate(zero(Gs)):
    print(f"Zero {i+1}: {z:.4}")

print("Polos Discretos")
for i , p in enumerate(pole(Gz_2)):
    print(f"Polo {i+1}: {p:.4}")

print("Zeros Discretos")

for i , z in enumerate(zero(Gz_2)):
    print(f"Zero {i+1}: {z:.4}")

plt.show()