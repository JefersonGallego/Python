# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:32:09 2022

@author: Sergio
"""
import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *
from controlcae import *


plt.close()

# Tclab
Ts=15
# Continuo
numc=[2.247]
denc=[213.168,1,]

# Discreto
numd=[0.056175,0.096621]
dend=[1,-0.9321,0]

Gs = tf(numc,denc)
Gz=tf(numd,dend,Ts)


k = 1

cG = series(k,Gz)
print(Gz)
bode(Gz)

# Analisis de Estabilidad
#gm, pm, Wcg, Wcp = margin(cG)
gm, pm, Wcg, Wcp = margin_plot(Gz)
print('Margen de Ganancia:', 20*np.log10(gm))
print('Margen de Fase:', pm)
print('Frecuencia de Cruce de Fase:', Wcg)
print('Frecuencia de Cruce de Ganancia:', Wcp)
plt.show()
