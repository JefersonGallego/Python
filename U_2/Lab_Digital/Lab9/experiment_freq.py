# -*- coding: utf-8 -*-
"""
Diagrama de Bode
¿Cómo se hace un diagrama de Bode?

@author: Sergio
"""

import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *

plt.close()

# Creamos una función de transferencia
# que representa mi sistema o mi máquina real

#Gr = tf(1, [1, 1])

a=[2.2357]
b=[237.840,1]
theta=3.8720
G = tf(a,b)

#Pade
numt, dent = pade(theta,1)
theta_1 = tf(numt, dent)
Gs_1 = series(G, theta_1)

#Retardo
tnum=[-theta/2,1]
tden=[theta/2,1]
theta_2 = tf(tnum,tden)
Gs_2 = series(G, theta_2)
print(G,Gs_1,Gs_2)

# La entrada de estimulo siempre es senoidal
#Frecuencia (Variar la Frecuencia)
ws = 10**-3# ws= 2*pi / Ts
#amplitud
A = 1
#fase
alpha = 0

# Vector Tiempo
t = np.arange(0,50/ws,0.1/ws)

#entrada 
u = A * np.sin(ws*t + alpha) # A*sen(wt)

#Salida de la planta
y, tout, xout = lsim(Gs_2, u, t)


plt.plot(t, u, '-r', t, y, '-b')
plt.plot((t[0],t[-1]),(0,0),'-k')
plt.plot((t[0],t[-1]),(A,A),'-k')
plt.plot((t[0],t[-1]),(-A,-A),'-k')
plt.title('Frequency Response', fontsize=16)
plt.ylabel('Amplitude', fontsize=14)
plt.xlabel('Time (s)', fontsize=14)
plt.legend(['Input', 'Out'])
plt.show()




