# -*- coding: utf-8 -*-
"""
Regresión Lineal de EDO de Vanderpol

@author: Sergio
"""


from scipy.integrate import  solve_ivp
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Regresion Vandelpol

# Programar la EDO
def vanderpol(t, x, p):
    #Renombrar las salidas
    x1 = x[0]
    x2 = x[1]
    mu = p[0]

    #Renombrar las entrada
    # Q = u

    #EDO
    dx1dt = x2
    dx2dt = mu*(1.0-x1**2)*x2-x1
    #salida
    dxdt = [dx1dt, dx2dt]
    return dxdt


#Condición inicial (Sistema NO rígido)
x0 = [2, 0]
mu = 1
g = 1;
p0 = [mu, ]

#Tiempo de integración
t = np.linspace(0, 30)


#Solucionar la EDO
t_span = [t[0], t[-1]]
sol = solve_ivp(vanderpol, t_span, x0, args=(p0,), t_eval=t)
x = sol.y


#Graficar
plt.plot(t,x[0],'b:',linewidth=3,label='Initial Guess')
#plt.plot(t,xreal,'r-',linewidth=3,label='from data')
#plt.plot(t,xopt[0],'k--',linewidth=3,label='Final Prediction')
plt.legend(loc='best')
plt.xlabel('Time (sec)')
plt.ylabel("Position - x")
plt.savefig("Vaderpol"+".png")
plt.show()
