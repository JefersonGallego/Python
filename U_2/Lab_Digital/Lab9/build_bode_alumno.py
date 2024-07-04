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

# Tclab
Ts=15
# Continuo
numc = [2.247]
denc = [213.168,1,]
theta = 9.6217
Gs = tf(numc,denc)

#Pade
numt, dent = pade(theta,1)
theta_1 = tf(numt, dent)
Gs_1 = series(Gs, theta_1)

#Retardo
tnum=[-theta/2,1]
tden=[theta/2,1]
theta_2 = tf(tnum,tden)
Gs_2 = series(Gs, theta_2)

print(Gs,Gs_1,Gs_2)

# Datos Experimentales
w   = [10**-3, 10**-2, 10**-1, 10**0, 10**1]
mag = [2.1734, 0.86560, 0.110694, 0.017369, 0.001689]
# fase = Delta tiempo * ws 
pha = [-0.238, -1.211, -2.078, -4.741, -5.56716]

magdB = list(map(lambda i: 20*np.log10(i), mag))
phad = list(map(lambda i: np.rad2deg(i), pha))
#
#plt.figure(1)
bode(Gs_1)
#plt.figure(2)
plt.subplot(211)
plt.semilogx(w, magdB)
plt.grid()
plt.ylabel('Magnitud (dB)')
plt.xlabel('Frecuencia (rad/s)')
plt.subplot(212)
plt.semilogx(w, phad)
plt.grid()
plt.ylabel('Fase (deg)')
plt.xlabel('Frecuencia (rad/s)')
plt.show()