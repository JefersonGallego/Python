# Pedro Alejandro Sanchez Osorio
# Victor Alfonso Moyano Echeverri
# Jeferson Gallego Chaverra


from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt 
import numpy as np
from scipy.optimize import minimize

# Tclab (U - a)

# Phenomenological model Tclab
def TcLab (t, x, u, p):
    
    x1 = x[0]
    a = p[0]
    U = p[1] 
    Qi = u 
    Ta = 30.50 + 273.15

    Cp = 500
    m = 0.004
    O = 5.67e-8
    A = 1.2e-3
    E = 0.9

    dT1dt = (a*Qi+ U*A* (Ta-x1)+ E*O*A* (Ta**4 -x1**4)) /(m*Cp)

    dTdt = dT1dt
    
    return dTdt

# Calculate Position 
def calc_position(t, p, Q, x0):
    y0 = list(x0)
    ym = np.ones(len(t))*x0[0]
    for i in range(len(t)-1):
        ts = [t[i], t[i+1]]     # Time Differential
        sol= solve_ivp(TcLab, ts, y0, method = 'RK45', args = (Q, p)) 
        y0 = sol.y[:, -1]
        ym[i+1]= y0[0]
    return ym

# Optimizacion     
def objetive(p):
    #
    x = calc_position(t, p, Q, x0)
    j = 0.0
    for i in range(len(t)):
        j = j + ((xreal[i] - x[i])/ xreal[i])**2
    return j

#25
#0.4143481  
#6.05406798
name = "UA"

# Parameters Initials
a = 0.014
U = 5

Q = 0.40
Ta = tinit = 30.50 + 273.15
x0 = [Ta]
p0 = [a, U]

data =np.loadtxt('40.txt',delimiter=',',skiprows=1)
t = data[:,0].T
xreal = data[:,2].T
xreal = xreal + 273.15

# Time de Integration
# t = np.linspace(0, 899)   

print(f'Initial SSE :{objetive(p0)}')

solution = minimize(objetive, p0, method='SLSQP')
p = solution.x
print(solution.message)

t_span =[t[0], t[-1]]

sol= solve_ivp(TcLab, t_span, x0, method = 'RK45', args = (Q, p0 ), t_eval = t) 
x = sol.y 

print(f'New Parameters: {p}')
print(f'Final SSE :{objetive(p)}')

solopt = solve_ivp(TcLab, t_span, x0, method = 'RK45', args = (Q, p ), t_eval = t) 
xopt = solopt.y 

# Plots
xreal = xreal - 273.15
xopt =  xopt  - 273.15

plt.plot(t, xreal, 'k', linewidth=3, label='Process Data')
#plt.plot (t, x[0], 'b-', linewidth=2, label= ' Initial Estiamte')
plt.plot (t, xopt[0], 'r--', linewidth=2, label='Final Prediction')
plt.title(r"(U) - ($\alpha$) = Step 25 % Optimization",fontsize = 14)
plt.legend(loc='best')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.grid()
plt.savefig(name+".png")
plt.show()