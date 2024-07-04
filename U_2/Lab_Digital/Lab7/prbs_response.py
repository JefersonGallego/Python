# -*- coding: utf-8 -*-
"""
PRBS response
Lab 7
"""
import tclab_cae.tclab_cae as tclab
import time
import matplotlib.pyplot as plt
import numpy as np
from prbs import create_prbs

def save_txt(t, u1, y1):
    data = np.vstack( (t, u1, y1) ) #Vertical stack
    data = data.T
    top = 'Time (sec),  Heater (%),  Temperature (C)'
    np.savetxt('prbs_3.txt', data, delimiter=',',header = top, comments='')

# Connect to Arduino
lab = tclab.TCLab_CAE()

#Turn LED
lab.LED(100)
print('LED On')

# Run in time (minutes)
run_time = 40.0 

# Transform into the number of cicles
loops = int(run_time * 60.0)
tm = np.zeros(loops)

# Temperature (C)
T1 = np.ones(loops) * lab.T1

# Manipulated variable (0 - 100)
Q1 = create_prbs(0, 15, 40, 10, 50, loops-30, 25);    

#Q1 = create_prbs(20, 15, 50, 10, 50, loops-30, 20);    #pbrs_1
#Q1 = create_prbs(0, 10, 30, 10, 50, loops-30, 20);   #pbrs _2


#Q1 = np.zeros(loops) 
#Q1[10:] = 40


print('Running Main Loop. CTRL + C to end.')
print('  Time   Q1   T1')
print(f'{tm[0]:6.1f} {Q1[0]:6.2f} {T1[0]:6.2f}')

#Crear plot
plt.figure(figsize=(10,7))
plt.ion() #Enable interactive mode
plt.show()


# Main Loop
start_time = time.time()
prev_time = start_time

try:
    for k in range(1, loops):
        #sleep time
        sleep_max = 1.0
        sleep = sleep_max - (time.time() - prev_time)
        if sleep >= 0.01:
            time.sleep(sleep - 0.01)
        else:
            time.sleep(0.01)
            
        # Record time and change in time
        t = time.time()
        prev_time = t
        tm[k] = t - start_time
        
        #Read Temperature
        T1[k] = lab.T1
        
        # write Heater (0 -100)
        lab.Q1( Q1[k] )
        
        print(f'{tm[k]:6.1f} {Q1[k]:6.2f} {T1[k]:6.2f}')
        
        #Plot
        plt.clf() #Clear current figure
        ax = plt.subplot(211)
        ax.grid()
        plt.title("Response to PRBS Input",fontsize = 14)
        plt.plot(tm[0:k], T1[0:k],'-k',label=r'$T_1$', \
                 linewidth = 2)
        plt.ylabel('Temperature (°C)', fontsize=14)
        plt.legend(loc='best')
        
        ax = plt.subplot(212)
        ax.grid()
        plt.plot(tm[0:k], Q1[0:k],'-b',label=r'$Q_1$ ', \
                 linewidth = 2)
        plt.ylabel('Heater (%)', fontsize=14)
        plt.xlabel('Time (s)', fontsize=14)
        plt.legend(loc='best')
        plt.draw()
        plt.pause(0.05)
        
    # Turn off heaters
    lab.Q1(0)
    lab.Q2(0)
    lab.LED(0)
    lab.close()
    save_txt(tm[0:k], Q1[0:k], T1[0:k])
    plt.savefig('prbs.png')   
        
except KeyboardInterrupt:
    print('Operación interrumpida por teclado')
    
    
finally:
    # Disconnect from Arduino
    lab.Q1(0)
    lab.Q2(0)
    lab.LED(0)
    lab.close()
    print('Shutting down')
    save_txt(tm[0:k], Q1[0:k], T1[0:k])
    plt.savefig('prbs.png')
    