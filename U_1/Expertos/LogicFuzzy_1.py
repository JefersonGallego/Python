from datetime import tzinfo
import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fz
import pandas as pd

#Primera parte
U = np.arange(25,75.001,0.001)    # Universo del discurso

Tbj= fz.trapmf(U,[25,25,30,37])   # Conjunto T° Bajas Trapesoidal
Tmd= fz.trimf(U,[30,37,50])       # Conjunto T° Medias Ttiangular
Tat= fz.trapmf(U,[37,50,75,75])   # Conjunto T° Altas Trapesoidal
ts= fz.smf(U,30,50)      # Funcion s
tz= fz.zmf(U,30,50)      # Funcion z
tgau = fz.gaussmf(U,50,4) # Gaussiana
tsig= fz.sigmoid(U,45,10)   # Sigmodal

plt.plot(U,ts)
plt.plot(U,tz)
plt.plot(U,tgau)
plt.plot(U,tsig)
plt.show()
