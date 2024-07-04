"""
PID Control - TCLAB

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
                    z - 0.9321  
    
@authors: Jeferson Gallego Chaverra
          Pedro Alejendro Snachez Osorio
          Victor Alfonso Moyano Echeverri 
"""
import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *
import tclab_cae.tclab_cae as tclab
import time
from FuncionesTCLab import *    

plt.close()
# Discrete Transfer Function:
Ts   = 15                              # Sampling
numz =  np.array([0.056175 , 0.096621])      # Numerator
denz =  np.array([1, -0.9321])         # Denominator
d    =  1                              # Delay
denzd = np.hstack((denz, np.zeros(d)))
Gz   =  tf(numz, denzd, Ts)
print(Gz)

# Continuous Transfer Function Parameters:
K = 2.2472
theta1 = 9.6217
tau = 213.1685

# Delay Correction
theta = theta1 + Ts/2

# Connect to Arduino
lab = tclab.TCLab_CAE()
start_time = time.time()
pre_time = start_time

# Sleep time
sleep_max = 1.0

# No-linear Model Parameters
Ta = lab.T3     # lab.T1
Tinit = lab.T1  # Initial Temperature

# Time
tsim = 1000                 # Simulation time (sec)
nit = int(tsim/1)           # Number of Iterations 


# Vectors
t = np.zeros(nit)           # Time Vector
u = np.zeros(nit)           # In Vector (Heater)
y = np.zeros(nit)           # Out Vector  (Temperature)
e = np.zeros(nit)           # Error Vector

# Setpoint
r = np.zeros(nit)           # Reference Vector
r[:] = Tinit                # Reference = Tinit
r[20:] = 90                 # Setpoint


# Method Control       
if metodo == 1: #Z&N
    if control == 1: # P
        kp = tau/(K*theta)
        ti = np.infty
        td = 0
        namectrl = 'ZN_P'
    elif control == 2: # PI
        kp = (0.9*tau)/(K*theta)
        ti = 3.3*theta
        td = 0
        namectrl = 'ZN_PI'
    else: # PID
        kp = (1.2*tau)/(K*theta)
        ti = 2*theta
        td = 0.5*theta
        namectrl = 'ZN_PID'

elif metodo == 2: # IAE
    if control == 1: # P
        print(" CHOOSE PI OR PID ")
        kp = 1
        ti = np.infty
        td = 0
        namectrl = 'IAE'
    elif control == 2: # PI
        A = 0.984
        B = -0.986
        C = 0.608
        D = -0.707
        kp = (1/K)*(A*(theta/tau)**B)        
        ti = tau / (C*(theta/tau)**D)
        td = 0
        namectrl = 'IAE_PI'
    else: # PID
        A = 1.435
        B = -0.921
        C = 0.878
        D = -0.749
        E = 0.482
        F = 1.137
        kp = (1/K)*(A*(theta/tau)**B)        
        ti = tau / (C*(theta/tau)**D)
        td = tau * (E*(theta/tau)**F)
        namectrl = 'IAE_PID'

elif metodo == 3: # ITAE
    if control == 1: # P
        print(" CHOOSE PI OR PID")
        kp = 1
        ti = np.infty
        td = 0
        namectrl = 'ITAE'
    elif control == 2: # PI
        A = 0.859
        B = -0.977
        C = 0.674
        D = -0.68
        kp = (1/K)*(A*(theta/tau)**B)        
        ti = tau / (C*(theta/tau)**D)
        td = 0
        namectrl = 'ITAE_PI'
    else: # PID
        A = 1.357
        B = -0.947
        C = 0.842
        D = -0.738
        E = 0.381
        F = 0.995
        kp = (1/K)*(A*(theta/tau)**B)        
        ti = tau / (C*(theta/tau)**D)
        td = tau * (E*(theta/tau)**F)
        namectrl = 'ITAE_PID'

elif metodo == 4: # C&C
    if control == 1: # P
        kp = (1.03+(0.35*(theta/tau)))*(tau/(K*theta))
        ti = np.infty
        td = 0
        namectrl = 'C&C_P'
    elif control == 2: # PI
        kp = (0.9+(0.083*(theta/tau)))*(tau/(K*theta))
        ti = (theta*(0.9+(0.083*(theta/tau)))) / (1.27+(0.6*(theta/tau)))
        td = 0
        namectrl = 'C&C_PI'
    else: # PID
        kp = (1.35+(0.25*(theta/tau)))*(tau/(K*theta))
        ti = (theta*(1.35+(0.25*(theta/tau)))) / (0.54+(0.33*(theta/tau)))
        td = (0.5*theta) / (1.35+(0.25*(theta/tau)))
        namectrl = 'C&C_PID'

else: # PA
    if control == 1: # P
        print(" CHOOSE PI ")
        kp = 1
        ti = np.infty
        td = 0
        namectrl = 'AP'
    elif control == 2: # PI
        # Objetivo al 70%
        Tss = (4*tau)*0.60
        Mp = 5
        ep = np.sqrt((np.log(Mp/100)**2) / (np.pi**2 + np.log(Mp/100)**2))
        wn = 3 / (ep*Tss)
        kp = ((2*ep*wn*tau)-1) / K
        ti = (kp*K) / ((wn**2)*tau)
        td = 0
        namectrl = 'AP_PI'  
    else:
        print(" CHOOSE PI ")
        kp = 1
        ti = np.infty
        td = 0
        namectrl = 'AP'
    
# Equations Discrete PID Control
q0 = kp*(1+ Ts/(2*ti) + td/Ts)
q1 = -kp*(1- Ts/(2*ti) + td/Ts)
q2 = (kp*td)/Ts

# Plot
plt.figure(figsize=(7,5))
plt.ion()                   # Enable interactive mode
plt.show()

try:
    #Closed Control Loop
    for k in range(nit):
        
        #Time Plot
        tm = delay_time(sleep_max, pre_time)
        pre_time = tm
        t[k] = np.round(tm - start_time) - 1
        
        # Y Real
        y[k] = lab.T1
        
        # Error
        e[k] = r[k] - y[k]
               
        # Control law 
        
        # Calculate U -- Time = Multiple Ts
        if t[k]%Ts == 0:
            u[k] = u[k-1] + q0*e[k] + q1*e[k-1] + q2*e[k-2]
        # U = U-1 -- Time =/ Multiple Ts 
        else:
            u[k] = u[k-1]

        # Saturation
        if u[k] > 100:
            u[k] = 100
        elif u[k] < 0:
            u[k] = 0

        # Write Heater Q1
        lab.Q1(u[k])
        
        # Plot
        plt.figure(1)
        ax=plt.subplot(2,1,1)
        ax.grid()
        plt.plot(t[0:k],r[0:k],'--r',linewidth=3)
        plt.plot(t[0:k],y[0:k],'k-',linewidth=3)
        plt.legend(['Setpoint', 'T1'])
        plt.ylabel('Temperature (°C)',fontsize=14)
        plt.xlabel('Time (s)',fontsize=14)
        plt.title(f' Control {namectrl} (Experimental)',fontsize=14)

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
    print('Operación interrumpida por teclado')
    
    
finally:
    # Disconnect from Arduino
    lab.Q1(0)
    lab.Q2(0)
    lab.LED(0)
    lab.close()
    tc = t[:k].copy()
    uc = u[:k].copy()
    yc = y[:k].copy()
    rc = r[:k].copy()
    print('Shutting down')
    #save_txt(t, u, y, namectrl+"Expe") 
    #plt.savefig(namectrl+".png")
