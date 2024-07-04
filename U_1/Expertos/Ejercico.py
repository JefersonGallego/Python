from datetime import tzinfo
from site import execsitecustomize
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fz
import pandas as pd

# Temperatura 5 a 75 °C
# U{-70<= X <= 70}
# Error = -25

U = np.arange(-70,70.001,0.001)    # Universo del discurso

etmn= fz.trapmf(U,[-70,-70,-50,-30])   # Error temperatura muy negativo
etne= fz.trimf(U,[-50,-30,0])          # Error temperatura negativo
etze= fz.trimf(U,[-30,0,30])           # Error temperatura zero
etpo= fz.trimf(U,[0,30,50])            # Error temperatura positivo
etmp= fz.trapmf(U,[30,50,70,70])       # Error temperatura muy positivo

#plt.plot(U,etmn)
#plt.plot(U,etne)
#plt.plot(U,etze)
#plt.plot(U,etpo)
#plt.plot(U,etmp)
#plt.show()
# https://www.lawebdelprogramador.com/foros/Python/691962-leer-txt-por-fila-y-columnas.html


# VALOR DE PERTENENCIA
e=-30
VL= fz.interp_membership(U,etze,e)

print(VL)


