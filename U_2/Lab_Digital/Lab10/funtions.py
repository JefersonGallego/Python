import numpy as np
from scipy.integrate import solve_ivp
import time

# Funtion Delay
def delay_time(sleep_max, prev_time):
    sleep = sleep_max - (time.time() - prev_time)
    if sleep >= 0.01:
        time.sleep(sleep - 0.01)
    else:
        time.sleep(0.01)
        
    # Record time and change in time
    t = time.time()
    return t

# Save Data
def save_txt(t,u1,y1,name):
    data = np.vstack((t,u1,y1))   # Vertical Stack
    data = data.T                 # Transpose Data
    top = 'Time (s), Heater (%), ' \
        + 'Temperature (°C)' 
    np.savetxt(f'{name}.txt',data,delimiter=',',header=top,comments='')

# EDO Tclab
def TC_LAB (t,x,u,tinit):
    
    x1 = x[0]       # 
    Qi = u          # Heater Outpu
    
    cp = 500        # Heat Capacity
    m = 0.004       # Mass
    S = 5.6e-8      # Stefan Boltzmann Constant
    A = 1.2e-3      # Area
    E = 0.9         # Emissivity
    a = 0.014       # Heater Factor
    U = 5           # Heat Transfer Coefficient
    Ta = tinit      # Initial Temperature
    
    #EDO
    dx1dt= (a*Qi+ U*A* (Ta-x1)+ E*S*A* ((Ta**4)-(x1**4))) / (m*cp)
    return dx1dt

# Calculate Temperature
def cal_Tclab(t, u, x0,tinit):
    y0 = list(x0)
    ym = np.ones(len(t))*x0[0]
    for i in range(len(t)-1):
        tspan = [t[i], t[i+1]]  
        sol= solve_ivp(TC_LAB, tspan, y0, method = 'RK45', args = (u[i],tinit)) 
        y0 = sol.y[:, -1]
        ym[i+1]= y0[0]
    return ym

