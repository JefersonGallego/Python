
import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *
import math as mt
import sympy as sy
x=sy.symbols('x')
A=np.array([])
B= np.array([])

def Periodo(num,den,θ,k):
    G = tf(num,den)
    KG=series(k,G)     # K*G
    H=feedback(KG,1)   # Retroalimentacion  
    print("G(s)")      # Gs
    print(G)
    print("G(s)*D(s)") # Gs*Ds
    print(KG)
    print("\nPolos:")  # Polos (Estabilidad)
    for i , p in enumerate(pole(G)):   # Polos
        print(f"Polo {i+1}: {p:.4}")

    print("\nZeros:")  # Zeros (Lugar de 1 infinito)
    for i , p in enumerate(zero(G)):   # Polos
        print(f"Zero {i+1}: {p:.4}")

    print("\nRetroaliemtacion:")   
    print(H)            # Gs*Ds/(1+Gs*Ds)  
     
    if len(den)==2:      # Primer Orden
        print("\nSistema de Primer Orden\n")

        # T Equivalente
        Te =den[0]/(den[-1]+num[0])
        Tmin=0.2*(Te+θ)     # T Min
        Tmax=0.6*(Te+θ)     # T Max
        print("Ts : T Equivalente:\n")
        print(f" Tequ:: {Te:.4}, Tsmin:{Tmin:.4}, Tsmax:{Tmax:.4}\n")
        
        # BW
        mag,phase,w=bode(H)         # Magnitud, Fase, Bode
        m0=mag[0]                    # Magnitud 0
        mwc=m0*0.707                 # Magnitud
        index = np.where(mag>=mwc)   # Datos mayores a mwc
        wc=w[index[0][-1]]           # 
        wmin=np.pi/(6*wc)            # Frecuencia Minima
        wmax=np.pi/(4*wc)            # Frecuencia Maxima
        print("Ts : Ancho de Banda:\n")
        print(f"W0: {m0:.4}, (0.707)*W0: {mwc:.4}, Wc: {wc:.4}, Tsmin:{wmin:.4}, Tsmax:{wmax:.4}\n")
              
    elif len(den)==3:    # Segundo Orden 
        print("\nSistema de Segundo Orden\n")

        # T Equivalente
        ξ=den[1]/(2*(mt.sqrt(den[-1]+num[0])))
        
        if ξ >= 1:      # 0<ξ<1
            Te= 2*ξ/(mt.sqrt(den[-1]+num[0]))    # 2ξ/√Wc 
        else:            #ξ>=1
            Te= 1/(ξ*(mt.sqrt(den[-1]+num[0])))  # 1/ξ√Wc 
       
        Tmin=0.2*(Te+θ)     # T Min
        Tmax=0.6*(Te+θ)     # T Max
        print("Ts : T Equivalente:\n")
        print(f"Amortiguamiento: {ξ:.4}, Tequ:: {Te:.4}, Tsmin:{Tmin:.4}, Tsmax:{Tmax:.4}\n")  

        #   BW
        mag,phase,w=bode(H)          # Magnitud, Fase, Bode
        m0=mag[0]                    # Wo
        mwc=m0*0.707                 # W0*.707
        index = np.where(mag>=mwc)   # Datos mayores a mwc
        wc=w[index[0][-1]]           
        wmin=np.pi/(6*wc)            # π/6*Wc
        wmax=np.pi/(4*wc)            # π/4*Wc
        print("Ts : Ancho de Banda:\n")
        print(f"W0: {m0:.4}, (0.707)*W0: {mwc:.4}, Wc: {wc:.4}, Tsmin:{wmin:.4}, Tsmax:{wmax:.4}\n")

def zoh(num,den,T): 
    h = tf(num,den)
    hd = c2d(h,T,'zoh')   
    print("G(s)")      
    print(h)
    print("G(z)")      
    print(hd)
    B = hd.num[0][0]      # B=[b0,b1]     #estraigo  de TF
    A = hd.den[0][0]      # A=[a0,a1,a2]
    return (B,A) 

def AlimentacionK(num,den,K,Ts):
    Gz=tf(num,den,Ts)
    KG=series(K,Gz)     # K*G
    HGZ=feedback(KG,1)   # Retroalimentacion  
    print("G(z)*D(z)") # Gs*Ds
    print(KG)
    print("\nRetroaliemtacion:")   
    print(HGZ)
    print("\nPolos:")  # Polos (Estabilidad)

    for i , p in enumerate(pole(HGZ)):   # Polos
            print(f"Polo {i+1}: {p:.4}")
    print(" ")        
#Limite  0
def limite_(num,den,u,x):
    F=((num[0])*u) / ((den[0]*(x**2))+(den[1]*(x))+(den[2]))
    L= sy.limit(F,x,0)
    print(f"Funcion: {F}")
    print(f"Limite {L}")
#Limite 1
def limite(num,den,U,x):
    F=(((num[0])*x+(num[1]))*U/((den[0]*(x**2))+(den[1]*(x))+(den[2])))
    L= sy.limit(F,x,1)
    print(f"Funcion: {F}")
    print(f"Limite {L}")
    print("")

#control avanzado
#Kp: 2.46410341442896
#taup: 293.9205329481613
#thetap: 0.8332835307529356

a=[1.0719]
b=[272.9819,1]
teta=3.7102

k=1

T=40

K=1.5
u=5

Periodo(a,b,teta,k)
B,A=zoh(a,b,T)
#AlimentacionK(B,A,K,T)
#limite_(a,b,u,x)
#limite(B,A,u,x)



