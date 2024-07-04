import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *
import math as mt
import sympy as sy

# FT Tclab

def heaviside(theta, t):
    """
    Parameters
    ----------
    theta : retardo del sistema
    t : vector de tiempo (simulación)
    Returns
    -------
    H(t-theta): Interruptor Heaviside
    """
    delay = np.empty_like(t)
    for i in range(len(t)):
        if t[i] < theta:
            delay[i] = 0.0
        else: delay[i] = 1.0
    return delay

def fopdt_plot(K, tau, theta, n):
    t = np.linspace(0, n, 100) # vector tiempo
    num=[K]
    den=[tau,1]
    G = tf(num,den)
        
    # calcula la respuesta ante entrada escalón
    y = K*(1.0 - np.exp(-(t-theta)/tau)) * heaviside(theta, t)
    
    # grafica la respuesta
    plt.figure(1)
    plt.ylabel('y(t)')
    plt.xlabel('t')
    plt.plot(t, y, 'r-.', linewidth=2, label=f'{K:.2}e^-{theta:.2}s / {tau:.2}s + 1')
    plt.title("FT Tclab") 
    plt.legend(loc = 'best')
    
    
K= 2.2472
tau= 213.1685
theta= 9.6217
n = 3000

fopdt_plot(K, tau, theta, n)

plt.show()
