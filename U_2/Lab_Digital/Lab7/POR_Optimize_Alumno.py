import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import minimize
from scipy.interpolate import interp1d


# First Order Differential Equation with Delay    
def fopdt(t,y,uf,Km,taum,thetam):
    # Arguments
    # y = Output
    # t = Time
    # uf = Linear input function (To make time shift)
    # Km = Gain
    # taum = Time Constant
    # thetam = Delay
    
    try:
        if (t-thetam) <= 0:      
            um = uf(0.0)
        else:
            um = uf(t-thetam)
    except:
        um = u0
    # Output Equation - Calculate Derivative
    dydt = (-(y-yp0) + Km * (um-u0))/taum
    return dydt

# Simulation of the first order system
def sim_model(x):
    # Argumentos de entrada
    Km = x[0]
    taum = x[1]
    thetam = x[2]
    # Vector de Salida
    ym = np.ones(ns) * yp0  # model
    # Condición Inicial
    y0 = [yp0]  # Temperature Iitial
    # Model Simulation (Integration)  
    for i in range(0,ns-1):
        ts = [t[i],t[i+1]]
        sol = solve_ivp(fopdt,ts, y0,args=(uf,Km,taum,thetam))
        y0 = sol.y[:, -1]
        ym[i+1] = y0[0]
    return ym

# Funtion Objetive
def objective(x):
    # Calcule
    obj = 0.0
    #  Model Simulation
    ym = sim_model(x)
    for i in range(len(ym)):
        obj = obj + ((yp[i] - ym[i]) / yp[i]) ** 2
        #obj = obj + (yp[i] - ym[i]) ** 2
    return obj

# Column 0 = time (t)
# Column 1 = Input (u - Heater)
# Column 2 = Output (yp - Temperature)

# Data 
data = np.loadtxt('T2_40.txt',delimiter=',',skiprows=1)
name = "T2_40_%_Step"

# IN y OUT Initial
u0 = data[0,1]
yp0 = data[0,2]

# Experiment data
t = data[:,0].T - data[0,0]
u = data[:,1].T
yp = data[:,2].T

# Iterations Numbers
ns = len(t)

# Linear interpolation of time with u (useful to involve the time delay)
uf = interp1d(t,u)

# Inicial
K = 2
tau = 200
theta = 0.2


#control avanzado
#Kp: 2.46410341442896
#taup: 293.9205329481613
#thetap: 0.8332835307529356

# T1
#Kp: 2.595838539900211
#taup: 283.7830085700075
#thetap: 0.61293425110015

# T2
#Kp: 1.071957560720483
#taup: 272.9819961110351
#thetap: 3.7102858162240424

x0 = np.zeros(3)
x0[0] = K # Km
x0[1] = tau # taum
x0[2] = theta # thetam

# OPTIMIZACION
print(f"Initial SEE: {objective(x0)}")


solution= minimize(objective,x0,method='SLSQP')
x=solution.x
print(solution.message)
print(f'Final SSE: {objective(x)}')

#x = list(x0)
print('Kp: ' + str(x[0]))
print('taup: ' + str(x[1]))
print('thetap: ' + str(x[2]))

ym1 = sim_model(x0)
ym2 = sim_model(x)

plt.figure()
plt.plot(t, yp, 'k', linewidth=3, label='Process Data') # Datos del Proceso
#plt.plot(t, ym1, 'b-', linewidth=2, label='Initial Estimate') # Estimada Inicial
plt.plot(t, ym2, 'r--', linewidth=1, label='FOFT Optimized') # FT POR Optimizada
plt.title(r"(K) - ($\tau$) - ($\theta$) = T2 40% Step Optimization",fontsize = 14)
plt.ylabel('Temperature (°C)')
plt.xlabel('Time (s)')
plt.legend(loc= 'best')
plt.grid()
plt.savefig(name+".png")
plt.show()