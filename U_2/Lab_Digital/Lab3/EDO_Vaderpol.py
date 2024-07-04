from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt 
import numpy as np

# EDO Vanderpol

def vanderpol(t, x,u, mu):  # (Tiempo, Salida, Entrada, Parametros)
    # Renombrar Salidas
    x1=x[0]
    x2=x[1]
    # Renombrar Entradas
    #Q=u

    # Funciones de Primer Orden
    dx1dt=x2
    dx2dt=mu*(1-x1**2)*x2-x1
    
    # Vector Solucion 
    dxdt=[dx1dt,dx2dt]
    return dxdt

rigido= True

x0=[2,0] # Condiciones iniciales
u=0
if rigido:
    t=[0,3000]
    mu=1000
    metodo='Radau'
else:
    t=[0,30]
    mu=1
    metodo='RK45'

# Solucion de EDO
SOL=solve_ivp(vanderpol,t,x0,method=metodo,args=(u,mu))

# Datos Grafica
y=SOL.y # Vector lleno de Datos
t=SOL.t

plt.plot (t, y[:][0])  # Todas la Fila - Columna 0
plt.xlabel('Time [s]')
plt.ylabel('Position [y]')
plt.title("EDO Vanderpol") 
plt.grid()
plt.show()
    





