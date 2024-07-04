# -*- coding: utf-8 -*-
"""
Estabilidad Diagramas Bloques
"""
import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *

# Tclab
Ts = 15
# Continuo
numc=[2.247]
denc=[213.168,1,]
Gs = tf(numc,denc,Ts)

k = 1
print("Polos Continuos")
for i , p in enumerate(pole(Gs)):
    print(f"Polo {i+1}: {p:.2}")

#Bloques en serie
KG=series(k,Gs)  # K*G
H=feedback(KG,1)
mt=feedback(k,Gs)   # Accion de control Salida u

print("G(s)")
print(Gs)
print("G(s)*D(s)")
print(KG)
print(" G(s)D(s) / 1+G(s)D(s)")
print(H)

#Respuestas
plt.figure(1)

y,ty=step(H)
plt.subplot(2,1,1)     # Divida la Figura 
plt.plot(ty,y)
u,tu=step(mt)
plt.subplot(2,1,2)     
plt.plot(tu,u)

plt.figure(2)
pzmap(Gs)
plt.figure(3)
pzmap(H)

plt.show()


