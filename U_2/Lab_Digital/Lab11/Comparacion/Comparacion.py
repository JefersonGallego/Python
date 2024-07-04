import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *
from scipy.integrate import solve_ivp

Ts = 15
tsim = 2000                 #Tiempo de simulacion (segundos)
nit = int(tsim/Ts)          #Numero de Iteraciones
#Vectores
t = np.arange(0, (nit)*Ts, Ts)  #Tiempo

data1  = np.loadtxt('C&C_P.txt',delimiter=',',skiprows=1) # 1
data2  = np.loadtxt('C&C_PI.txt',delimiter=',',skiprows=1) # 3
data3  = np.loadtxt('C&C_PID.txt',delimiter=',',skiprows=1) #8
data4  = np.loadtxt('IAE_PI.txt',delimiter=',',skiprows=1) # 4
data5  = np.loadtxt('IAE_PID.txt',delimiter=',',skiprows=1)#9
data6  = np.loadtxt('ITAE_PI.txt',delimiter=',',skiprows=1) # 5
data7  = np.loadtxt('ITAE_PID.txt',delimiter=',',skiprows=1) #10
data8  = np.loadtxt('ZN_P.txt',delimiter=',',skiprows=1) # 2
data9  = np.loadtxt('ZN_PI.txt',delimiter=',',skiprows=1)# 6
data10 = np.loadtxt('ZN_PID.txt',delimiter=',',skiprows=1) #11
data11 = np.loadtxt('AP_PI.txt',delimiter=',',skiprows=1) # 7

u1 = data1[:,1].T
y1 = data1[:,2].T

u2 = data2[:,1].T
y2 = data2[:,2].T

u3 = data3[:,1].T
y3 = data3[:,2].T

u4 = data4[:,1].T
y4 = data4[:,2].T

u5 = data5[:,1].T
y5 = data5[:,2].T

u6 = data6[:,1].T
y6 = data6[:,2].T

u7 = data7[:,1].T
y7 = data7[:,2].T

u8 = data8[:,1].T
y8 = data8[:,2].T

u9 = data9[:,1].T
y9 = data9[:,2].T

u10 = data10[:,1].T
y10 = data10[:,2].T

u11 = data11[:,1].T
y11 = data11[:,2].T

Tambiente = 30
Referencia = 80

#  Conviento a °K
Tinit = Ta = Tambiente 

x0=[Ta]
r = np.zeros(nit)
r[:] = Tinit
ref = r[5:] = Referencia

#P
plt.figure(1)
ax=plt.subplot(2,1,1)
ax.grid()
plt.plot(t,r,'r--', linewidth=3)
plt.plot(t,y1,'b',t,y8,'y--', linewidth=2)
plt.legend(['Ref','C&C_P','ZN_P'],loc = 1,fontsize=12)
plt.ylabel('Temperature (°C)',fontsize=16)
plt.title(f'Control P (Simulation)',fontsize=16)

ax=plt.subplot(2,1,2)
ax.grid()
plt.plot(t,u1,'b',t,u8,'y--', linewidth=2)
plt.legend(['C&C_P','ZN_P'],loc = 1,fontsize=12)
plt.ylabel('Heater (%)',fontsize=16)
plt.xlabel('Time (s)',fontsize=16)

# PI
plt.figure()
ax=plt.subplot(2,1,1)
ax.grid()
plt.plot(t,r,'r--', linewidth=3)
plt.plot(t,y2,'k', t,y4,'b--', t,y6,'g', t,y9,'y--', t,y11,'m',linewidth=2)
plt.legend(['Ref','C&C_PI','IAE_PI','ITAE_PI','ZN_PI','AP_PI'],loc = 4,fontsize=12)
plt.ylabel('Temperature (°C)',fontsize=16)
plt.title(f'Control PI (Simulation)',fontsize=16)

ax=plt.subplot(2,1,2)
ax.grid()
plt.plot(t,u2,'k', t,u4,'b--', t,u6,'g', t,u9,'y--', t,u11,'m',linewidth=2)
plt.legend(['C&C_PI','IAE_PI','ITAE_PI','ZN_PI','AP_PI'],loc = 4,fontsize=12)
plt.ylabel('Heater (%)',fontsize=16)
plt.xlabel('Time (s)',fontsize=16)

# PID
plt.figure()
ax=plt.subplot(2,1,1)
ax.grid()
plt.plot(t,r,'r--', linewidth=3)
plt.plot(t,y3,'k', t,y5,'b--', linewidth=3)
plt.plot(t,y7,'g',linewidth=2)
plt.plot(t,y10,'y--', linewidth=2)
plt.legend(['Ref','C&C_PID','IAE_PID','ITAE_PID','ZN_PID'],loc = 4,fontsize=12)
plt.ylabel('Temperature (°C)',fontsize=16)
plt.title(f'Control PID (Simulation)',fontsize=16)

ax=plt.subplot(2,1,2)
ax.grid()
plt.plot(t,u3,'k', t,u5,'b--', linewidth=3)
plt.plot(t,u7,'g', linewidth=2)
plt.plot(t,u10,'y--', linewidth=2)
plt.legend(['C&C_PID','IAE_PID','ITAE_PID','ZN_PID'], loc = 4,fontsize=12)
plt.ylabel('Heater (%)',fontsize=16)
plt.xlabel('Time (s)',fontsize=16)

plt.show()


