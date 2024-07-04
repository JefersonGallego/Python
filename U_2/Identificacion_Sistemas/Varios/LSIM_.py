import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *
from scipy.integrate import solve_ivp

def sim(self, t, U = []):
        """
        Simulate the PLL with a input

        Parameters
        ----------
        t : array_like
            Vector with the time
        U: array_like
            Input to the block with the same lenght of t, if a empty is given

        Return
        ------
        out : array like response to U
        error : error
        """
        if not len(U):
            U = np.ones_like(t)
        t, signal_out, X = lsim(self, U=U, T=t)
        return signal_out, t

Ts=5
tsim = 500                 #Tiempo de simulacion (segundos)
nit = int(tsim/Ts)          #Numero de Iteraciones

#Vectores
t = np.arange(0, (nit)*Ts, Ts)  #Tiempo
u = np.ones(nit)*5           #Vector de entrada (Heater)

num = [5]
den = [1,3,2]

a=[2.1273]
b=[222.6246,1]
sys = tf(a,b)
print(sys)

y,t=sim(sys,t,u)

plt.plot(y,t)
plt.grid()
plt.show()
