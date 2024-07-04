

import matplotlib.pyplot as plt
import numpy as np
from control.matlab import *
from scipy.integrate import odeint


#F = 10 #Frecuencia
T = .16

# PBRS
#Kp: 2.2472328285247647
#taup: 213.16858982908337
#thetap: 9.621762010893972

#a=[2.247]
#b=[213.168,1]


a=[2.2462]
b=[0.4993,1]
h = tf(a,b)

#Pade
numt, dent = pade(3.8720,1)
theta_1 = tf(numt, dent)
h1 = series(h, theta_1)

#Agr Pade
td_p=1
np_exp=[-td_p/3.8720,1]
dp_exp=[td_p/3.8720,1]
theta_2=tf(np_exp,dp_exp)
h2 = series(h,theta_2)

# Discretizacion
hd = c2d(h,T,'zoh')   # c2d(Gp(s),T,"Metodo")
hd1 = c2d(h,T,'foh') 
hd2 = c2d(h,T,'zoh') 
print(h)
print(hd)


y,t = step(h) 
yd,td = step(hd)
yd1,td1 = step(hd1)   
yd2,td2 = step(hd2)   

plt.plot(t,y,   'k', linewidth=1, label='Continue') 
plt.step(td,yd, 'r', linewidth=1, label='ZOH')
#plt.step(td1,yd1, label='FOH')
#plt.step(td2,yd2, label='Tustin')
plt.title("Discretization and Sampling G(s)",fontsize = 14)
plt.ylabel(' Y(t) ',fontsize = 12)
plt.xlabel(' Time (s) ',fontsize = 12)
plt.legend(loc='best')
plt.grid()
plt.show()

#  Implementación del modelo en sistemas embebidos

nit = int(10/0.1)    # Periodo de Tiempo de Simulacion  
y = np.zeros(nit)    # Vector de Sensor
u = np.zeros(nit)    # Vector Accion de Control
u[10:] =1            # Aplicacion  del Escalon
t = np.arange(0,(nit)*0.1,0.1)    # Vector tiempo 

B = hd.num[0][0]      # B=[b0,b1]     #estraigo  de TF
A = hd.den[0][0]      # A=[a0,a1,a2]
d = 0                 # Retardo

for k in range(2,nit):
    y[k]= -A[1]*y[k-1] - A[2]*y[k-2] + B[0]*u[k-1-d] + B[1]*u[k-2-d]

plt.figure()
plt.plot(t,y,'--')
plt.show()