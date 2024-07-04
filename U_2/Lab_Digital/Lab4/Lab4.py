from control.matlab import *
import numpy as np
import matplotlib.pyplot as pt 

def muestreo_banda(Cs,Gs):
    Hs= feedback(series(Cs,Gs))  # Lazo Cerrado
    mag,phase,w=bode(Hs)         # Magnitud, Fase, Bode
    m0=mag[0]                    # Magnitud 0
    mwc=m0*0.707                 # Magnitud
    index = np.where(mag>=mwc)   # Datos mayores a mwc
    wc=w[index[0][-1]]           # 
    wmin=np.pi/(6*wc)            # Frecuencia Minima
    wmax=np.pi/(4*wc)            # Frecuencia Maxima
    Ts=(wmin+wmax)/2

    print(f"Retroalimentacion: {Hs} W0: {m0}  (0.707)W0: {mwc}") 
    print(f"Wc {wc} Tmin {wmin}  Tmax {wmax}")


# Planta en Lazo Abierto
num=[0.0414,0.00111]           # Numerador
den=[1,-0.62,0.000000000000058]     # Denominador
G=tf(num,den)   # Funcion de Transferencia 
muestreo_banda(1,G)
