from control.matlab import *
import numpy as np
import matplotlib.pyplot as pt 


# JEFERSON GALLEGO CHAVERRA
# PEDRO ALEJANDRO SANCHES OSORIO
# VICTOR ALFONSO MOYANO ECHEVERRI 

# Tiempo de Muestreo

# Ancho de Banda
def muestreo_banda(Cs,Gs):
    Hs= feedback(series(Cs,Gs))  # Lazo Cerrado
    mag,phase,w=bode(Hs)         # Magnitud, Fase, Bode
    m0=mag[0]                    # Magnitud 0
    mwc=m0*0.707                 # Magnitud
    index = np.where(mag>=mwc)   # Datos mayores a mwc
    wc=w[index[0][-1]]           
    wmin=np.pi/(6*wc)            # Frecuencia Minima
    wmax=np.pi/(4*wc)            # Frecuencia Maxima
    Ts=(wmin+wmax)/2             #
    return Ts                    # Retorno Periodo BW

# Tiempo de Establecimiento Primero Orden 
def FO(Cs,Gs):
    Hs= feedback(series(Cs,Gs))  # Lazo Cerrado
    [Num,Den]=tfdata(Hs)         # Sacar datos LC
    index = np.where(Den)
    Den2 = Den[index[0][-1]]
    Den3 = Den2[index[0][-1]]
    Den0=Den3/Den3[1]
    Tau = Den0[0]
    Tss = 5*Tau
    Tmin = Tss/20
    Tmax = Tss/10
    T = (Tmin + Tmax) /2
    return T

# Tiempo de Establecimiento Segundo Orden 
def SO(Cs,Gs):
    Hs= feedback(series(Cs,Gs))  # Lazo Cerrado
    [Num,Den]=tfdata(Hs)         # Sacar datos
    index = np.where(Den)
    Den2 = Den[index[0][-1]]
    Den3 = Den2[index[0][-1]]
    Den0=Den3/Den3[0]            
    wn=(Den0[2])**(0.5)
    e=Den0[1]/(2*wn)
    
    if e >=1:
        Tau=(2*e)/wn 
    else:
        Tau=1/(e*wn)  
    
    Tss = 5*Tau
    Tmin = Tss/20
    Tmax = Tss/10
    T = (Tmin + Tmax) /2
    return T

# Tiempo de Establecimiento Orden Superior 
def FOSO(Cs1,Gs1,Cs2,Gs2):
    # FT Primer Orden
    Hs1 = feedback(series(Cs1,Gs1))  # Lazo Cerrado
    [Num1,Den1]=tfdata(Hs1)     # Sacar datos
    index = np.where(Den1)
    Dena = Den1[index[0][-1]]
    Denb = Dena[index[0][-1]]
    Den0 =Denb/Denb[1]
    Tau1 = Den0[0]  
    # FT Segundo Orden
    Hs2 = feedback(series(Cs2,Gs2))  # Lazo Cerrado
    [Num2,Den2]=tfdata(Hs2)         # Sacar datos
    index = np.where(Den2)
    Denc = Den2[index[0][-1]]
    Dend = Denc[index[0][-1]]
    Den01=Dend/Dend[0]            
    wn=(Den01[2])**(0.5)
    e=Den01[1]/(2*wn)
    
    if e >=1:
        Tau2=(2*e)/wn 
    else:
        Tau2=1/(e*wn)

    Tau = Tau1 + Tau2
    Tss = 5*Tau
    Tmin = Tss/20
    Tmax = Tss/10
    T = (Tmin + Tmax) /2
    return T
    
print("Primer Sistema:")
num1=[1,0.5]          # Numerador
den1=[1,0.2]     # Denominador
G1=tf(num1,den1)   # Funcion de Transferencia 
T1TSS = FO(1,G1)
T1BW = muestreo_banda(1,G1)
print(f'{G1}')
print(f'Tiempo de muestreo por BW: {T1BW}, Tiempo de muestreo por TSS: {T1TSS}\n')
      
print("Segundo Sistema")
num2=[0.1429]
den2=[1,3.57,2.86]
G2=tf(num2,den2)
T2TSS = SO(1,G2)
T2BW = muestreo_banda(1,G2)
print(f'{G2}')
print(f'Tiempo de muestreo por BW: {T2BW}, Tiempo de muestreo por TSS: {T2TSS}\n')

print("Tercer Sistema")
num3a=[2.6]
den3a=[1, 2]
den3BW = [1, 10, 32, 32]
G33=tf(num3a,den3BW)
G3BW = tf(num3a, den3BW)
T3BW = muestreo_banda(1,G3BW)

num3b= [1]
den3b = [1, 8, 16]
G3a = tf(num3a, den3a)
G3b= tf(num3b, den3b)
T3TSS = FOSO(1,G3a,1,G3b)
print(f'{G33}')
print(f'Tiempo de muestreo por BW: {T3BW}, Tiempo de muestreo por TSS: {T3TSS}\n')

