"""
Proportional Control - TCLAB

Parameters FOTF
K: 2.2472
tau: 213.1685
theta: 9.6217

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
import tclab_cae.tclab_cae as tclab
from funtions import * 
    
plt.close()

# Discrete Transfer Function:
Ts   = 15                              # Sampling
numz =  np.array([0.056175 , 0.096621])      # Numerator
denz =  np.array([1, -0.9321])         # Denominator
d    =  1                              # Delay
denzd = np.hstack((denz, np.zeros(d)))
Gz   =  tf(numz, denzd, Ts)
print(Gz)
kss = dcgain(Gz) 


# Connect to Arduino
lab = tclab.TCLab_CAE()
start_time = time.time()
prev_time = start_time

# Sleep Time
sleep_max = 1.0

# No-linear Model Parameters
Ta = lab.T3      # Ambient Temperature
Tinit = lab.T1   # Initial Temperature

# Time
tsim = 700                 # Simulation Time 
nit = int(tsim/1)          # Number of Iterations
t = np.zeros(nit)          # Time Vector

# Vectors
u = np.zeros(nit)          # In Vector (Heater)
y = np.zeros(nit)          # Out Vector (Temperature)
e = np.zeros(nit)          # Error Vector

# Setpoint
r = np.zeros(nit)          # Reference Vector
r[:] = Tinit               # Reference = Tinit
r[20:] = 80                # Setpoint

# Proportional Control
Kc = 6                     # Gain
bias = 0                   # Bias = 0

# Plot
plt.figure(figsize=(7,5))
plt.ion()                # Enable interactive mode
plt.show()

try:
    # Closed Control Loop
    for k in range(nit):
        
        # Time
        tm = delay_time(sleep_max, prev_time)
        prev_time = tm
        t[k] = np.round(tm - start_time) - 1
        
        # Y Real
        y[k] = lab.T1
        
        # Error
        e[k] = r[k] - y[k]
        
        # Control Law
        
        # Bias
        bias= (y[k]-y[0])/ kss 
        
        # Calculate U -- Time = Multiple Ts
        if t[k]%Ts == 0:
            u[k] = Kc*e[k] + bias
        #  U = U-1 -- Time =/ Multiple Ts 
        else:
            u[k] = u[k-1]
        
        # Saturation
        if u[k] > 100:
            u[k] = 100
        elif u[k] < 0:
            u[k] = 0

        # Write Heater (0 -100)
        lab.Q1(u[k])
        
        # Plot
        plt.figure(1)
        ax=plt.subplot(2,1,1)
        ax.grid()
        plt.plot(t[0:k],r[0:k],'--r',linewidth=3)
        plt.plot(t[0:k],y[0:k],'k-',linewidth=3)
        plt.legend(['Setpoint', ''])
        plt.ylabel('Temperature (°C)',fontsize=14)
        plt.xlabel('Time (s)',fontsize=14)
        plt.title(f'Proportional Control K= {Kc} (Experimental)',fontsize=14)

        ax=plt.subplot(2,1,2)
        ax.grid()
        plt.step(t[0:k],u[0:k],'b-',linewidth=3)
        plt.legend(['Q1'])
        plt.ylabel('Heater (%)',fontsize=14)
        plt.xlabel('Time (s)',fontsize=14)
        plt.draw()
        plt.pause(0.05)
            
    # Turn off heaters
    lab.Q1(0)
    lab.Q2(0)
    lab.LED(0)
    
 
# Allow user to end loop with Ctrl-C          
except KeyboardInterrupt:
    print('Operation interrupted by keyboardo')
    
    
finally:
    # Disconnect from Arduino
    lab.Q1(0)
    lab.Q2(0)
    lab.LED(0)
    lab.close()
    print('Shutting down')
    name = "Control_P"
    #save_txt(t, u, y,name)
    #plt.savefig(name+".png")
