# -*- coding: utf-8 -*-
"""
Estabilidad por el lugar geométrico de las raíces

Pedro Alejandro Sanchez Osorio
Victor Alfonso Moyano Echeverri
Jeferson Gallego Chaverra
"""

import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *


# Tclab
Ts=15
# Discreto
numd=[0.056175,0.096621]
dend=[1,-0.9321,0]
Gs = tf(numd,dend,Ts)

print(Gs)
rlocus(Gs,grid=True)
plt.show()

#Respuestas
"""
plt.figure(2)
ax=plt.subplot(2,1,1)
ax.grid()
plt.title("Respuestas Dinamicas", fontsize = 14)
y,ty=step(H) 
plt.plot(ty,y)
plt.ylabel('Respuesta Sistema', fontsize = 10)   
ax=plt.subplot(2,1,2)
ax.grid()
u,tu=step(mt)     
plt.plot(tu,u)
plt.ylabel('Accion de Control', fontsize = 10)
plt.xlabel('Time (s)', fontsize = 10)
"""