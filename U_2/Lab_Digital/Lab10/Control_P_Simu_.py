"""
Proportional Control Simulation - TCLAB

Parameters FOTF
K: 2.2472
tau: 213.1685
theta: 9.6217

Continuous Transfer Function:
                   2.2472 exp(-9.6217s)
    G(s) =  ----------------------
                213.1685 s + 1

Discrete Transfer Function:
                 0.056175z + 0.096621 
G(z) = z^(-1) * ---------------------   Ts = 15
                    z - -0.9321  
    
@authors: Jeferson Gallego Chaverra
          Pedro Alejendro Snachez Osorio
          Victor Alfonso Moyano Echeverri 
"""
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *
from scipy.integrate import solve_ivp

# Import calTclab,TC_LAB
from funtions import * 

name = "Simulation_P"


# Discrete Transfer Function:
Ts   = 15                              # Sampling
numz =  np.array([0.056175 , 0.096621])      # Numerator
denz =  np.array([1, -0.9321])         # Denominator
d    =  1                              # Delay
denzd = np.hstack((denz, np.zeros(d)))
Gz   =  tf(numz, denzd, Ts)
print(Gz)
kss = dcgain(Gz)

# No-linear Model Parameters

# Reference Temperature °C
Tam = 35             # Initial Temperature
Ref = 80             # Reference Temperature 

# Conversion in °K
Tinit = Ta = Tam + 273.15
x0=[Ta]

# Time
tsim = 900              # Simulation time (sec)
nit = int(tsim/Ts)      # Number of Iterations 

# Vectors
t = np.arange(0, (nit)*Ts, Ts)  # Time Vector
u = np.zeros(nit)           # In Vector (Heater)
y = np.zeros(nit)           # Out Vector  (Temperatur3)
y[:] = Tinit                # y[0]= T initial
e = np.zeros(nit)           # Error Vector
q = np.zeros(nit)           # Riot Vector
q[35:] = 8

# Setpoint
r = np.zeros(nit)           # Reference Vector
r[:] = Tinit                # Reference = Tinit
ref = r[5:] = Ref + 273.15  # Setpoint

# Proportional Control
Kc = 9                      # Gain
bias = 0                    # Bi0 0as

#Closed Control Loop
for k in range(nit):
    
    # Simulation Non-Linear Model 
    if k > 1:
        T1 =cal_Tclab(t[0:k+1], u[0:k+1] - q[0:k+1], x0[0:k+1], Tinit)
        y[k] = T1[-1]
    
    # Error 
        e[k] = r[k] - y[k]
    
    # Control Law 
        bias= (y[k]-y[0])/ kss 

        u[k] = Kc*e[k] + bias
        
    # Saturation  
        if u[k] > 100:
            u[k] = 100
        elif u[k] < 0:
            u[k] = 0

# Conversion in °C
y=y-273.15
r=r-273.15

#Graph 
plt.figure()

ax=plt.subplot(2,1,1)
ax.grid()
plt.plot(t,r,'r--',t,y,'k-',linewidth=3)
plt.legend(['Setpoint', 'T1'])
plt.ylabel('Temperature (°C)',fontsize=14)
plt.xlabel('Time (s)',fontsize=14)
plt.title(f'Proportional Control K = {Kc} (Simulation)',fontsize=14)

ax=plt.subplot(2,1,2)
ax.grid()
plt.step(t,u,'b-',linewidth=3)
plt.legend(['Q1'])
plt.ylabel('Heater (%)',fontsize=14)
plt.xlabel('Time (s)',fontsize=14)

#plt.savefig(name+".png")
#save_txt(t, u, y_1,name)
plt.show()





