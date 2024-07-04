# -*- coding: utf-8 -*-

"""
LABORATORIO N° 5 CONTROL DIGITAL
Respuesta ante un escalon en la entrada del TCLab
by Sergio Castaño
Lab 5 - Control Digital

JEFERSON GALLEGO CHAVERRA
PEDRO ALEJANDRO SANCHEZ OSORIO
VICTOR ALFONSO MOYANO ECHEVERRI
"""

import tclab_cae.tclab_cae as tclab    
import time
import numpy as np
import matplotlib.pyplot as plt


# save txt file
def save_txt(t,u1,y1):
    data = np.vstack((t,u1,y1))  # vertical stack
    data = data.T                 # transpose data
    top = 'Time (s), Heater (%), ' \
        + 'Temperature (°C)' 
    np.savetxt(f'{w}.txt',data,delimiter=',',header=top,comments='')
    

#Modifica el tamaño de los ejes en todo el notebook
plt.rcParams.update({'font.size':14})

# Connect to Arduino
lab = tclab.TCLab_CAE()

# Turn LED on
print('LED On')
lab.LED(100)

# Run time in minutes
run_time = 60

# Transform into the Number of cycles
loops = int(60.0*run_time)
tm = np.zeros(loops)

# Temperature (C)
T1 = np.ones(loops) * lab.T3 # measured T (degC)

# impulse tests (0 - 100%)
Q1 = np.zeros(loops) * 0.0

Q1[20:] = 40.0  #Escalon 

w=int(Q1[-1])

print('Running Main Loop. Ctrl-C to end.')
print('  Time   Q1    T1')
print(f'{tm[0]:6.1f} {Q1[0]:6.2f} {T1[0]:6.2f}')

# Create plot
plt.figure(figsize=(10,7))
plt.ion() #Enable interactive mode.
plt.show()

# Main Loop
start_time = time.time()    # Inicio el Tiempo
prev_time = start_time      
"""
try if you: 
    do 'Ctrl+C
    disconnect the lab
"""
try: #Try - Except
    for k in range(1,loops):
        # Sleep time - Control the time of the graph
        sleep_max = 1.0 # Decrease if you want faster graph
        sleep = sleep_max - (time.time() - prev_time)
        if sleep>=0.01:
            time.sleep(sleep-0.01)
        else:
            time.sleep(0.01)

        # Record time and change in time
        t = time.time()
        dt = t - prev_time
        prev_time = t
        tm[k] = t - start_time

        # Read temperatures in Celsius
        T1[k] = lab.T3

        
        # Write output (0-100)
        lab.Q2(Q1[k])

        # Print line of data
        print(f'{tm[k]:6.1f} {Q1[k]:6.2f} {T1[k]:6.2f}')
        
        # Plot
        plt.clf() #Clear the current figure.
        ax=plt.subplot(2,1,1)
        ax.grid()
        plt.title(f"Response to {w} % Step Input",fontsize = 14)
        plt.plot(tm[0:k],T1[0:k],'k-',label=r'$T_2$', \
                 linewidth = 2)
        plt.ylabel('Temperature (°C)', fontsize = 14)
        plt.legend(loc='best')
        
        ax=plt.subplot(2,1,2)
        ax.grid()
        plt.plot(tm[0:k],Q1[0:k],'b-',label=r'$Q_2$', \
                 linewidth = 2)
        plt.ylabel('Heater (%)', fontsize = 14)
        plt.xlabel('Time (s)', fontsize = 14)
        plt.legend(loc='best')
        plt.draw()
        plt.pause(0.05)

    # Turn off heaters
    lab.Q1(0)
    lab.Q2(0)
    # Save text file
    save_txt(tm[0:k],Q1[0:k],T1[0:k])
    # Save figure
    plt.savefig(f'{w}.png')

# Allow user to end loop with Ctrl-C          
except KeyboardInterrupt:
    # Disconnect from Arduino
    lab.Q1(0)
    lab.Q2(0)
    print('Shutting down')
    lab.close()
    save_txt(tm[0:k],Q1[0:k],T1[0:k])
    plt.savefig(f'{w}.png')

# Make sure serial connection still closes when there's an error
except:          
    # Disconnect from Arduino
    lab.Q1(0)
    lab.Q2(0)
    print('Error: Shutting down')
    lab.close()
    save_txt(tm[0:k],Q1[0:k],T1[0:k])
    plt.savefig(f'{w}.png')
    raise