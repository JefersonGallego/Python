from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt 
import numpy as np

# EDO Tclab

def TC_LAB (t,x,Qi,Ta):
    
    alfa=0.014
    cp=500
    m=0.004
    KS=5.6e-8
    A=1.2e-3
    U=5
    E=0.9
    
    x1=x[0]

    #EDO
    dx1dt= (alfa*Qi+U*A*(Ta-x1)+E*KS*A*((Ta**4)-(x1**4)))/(m*cp)
    
    return dx1dt

Ta=296
x0= [Ta]
Qi=10

t_span=[0,1200]
pts= int(t_span[-1]/0.1) #define tiempo de muestreo 0.1 hasta la posicion 30
time_eval= np.linspace(0,1200,pts) #genera lista con todos los numeros igual/ espaciados (300 pts)
metodo='RK45'

sol= solve_ivp(TC_LAB, t_span, x0, method=metodo,args=(Qi,Ta),t_eval=time_eval) #se guarda la solucion pero hay varios datos   

y= sol.y #contiene varios tipos de datos, accede a la solucion de la EC 
t=sol.t
#graficas
y=y-273
plt.plot (t, y[:][0]) 
plt.xlabel('Time [s]')
plt.ylabel('Temperature [°K]')
plt.title("EDO Tclab",fontsize = 14)
plt.title("EDO Tc_Lab") 
plt.grid()
plt.show()
    