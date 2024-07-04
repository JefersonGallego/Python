"""
ARX Estimation - Tclab

@authors: Jeferson Gallego Chaverra
          Pedro Alejandro Sanchez Osorio
          Victor Alfonso Echeverri Moyano
"""
import numpy as np
import matplotlib.pyplot as plt
import control as cl
import math as ma
import sympy as sym
from sklearn.metrics import *
from Funtions import *


data = np.loadtxt('1.txt',delimiter=',',skiprows=1)

data1 = np.loadtxt('2.txt',delimiter=',',skiprows=1)

# Tclab Data
t1 = data[:,0].T 
u1 = data[:,1].T
y1 = data[:,2].T

t2 = data1[:,0].T 
u2 = data1[:,1].T
y2 = data1[:,2].T


 
# Subplot Data
ax=plt.subplot(2,1,1)
ax.grid()
plt.title("Response to 40 % Step Input ",fontsize = 14)
plt.plot(t2, y2, 'k', linewidth=2, label=r'$T1$')
plt.ylabel('Temperature (°C)', fontsize = 14)
plt.legend(loc='best')
"""
ax=plt.subplot(2,2,2) 
ax.grid()
plt.title("Response to 40 % Step Input ",fontsize = 14)
plt.plot(t2, y2, 'k', linewidth=2, label=r'$T1$')
plt.ylabel('Temperature (°C)', fontsize = 14)
plt.legend(loc='best')
"""
# Subplot Step          
ax=plt.subplot(2,1,2)
ax.grid()
plt.plot(t2, u2, 'b-', linewidth=2, label=r'$Q1$')
plt.ylabel('Step (%)', fontsize = 14)
plt.xlabel('Time (s)', fontsize = 14)
plt.legend(loc='best')

"""
ax=plt.subplot(2,2,4)
ax.grid()
plt.plot(t2, u2, 'b-', linewidth=2, label=r'$Q1$')
plt.ylabel('Step (%)', fontsize = 14)
plt.xlabel('Time (s)', fontsize = 14)
plt.legend(loc='best')
"""
plt.show()