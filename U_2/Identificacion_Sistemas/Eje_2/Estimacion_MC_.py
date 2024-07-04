# EJERCICIO 2   Estimacion por Minimos Cuadrados

# JEFERSON GALLEGO, PEDRO SANCHEZ, VICTOR MOYANO

from sympy import MatrixSymbol, Matrix, Identity
import sympy as sym

sym.init_printing()
#%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# FUNCIONES 
# Valida datos numericos
def validar_Dato(frase):

    while True:
            valor= input(frase)     
            if valor.isnumeric():
                valor = int(valor)
                break
            else:
                print('El dato ingresado no es numerico , por favor ingresar un dato numerico')

    return valor
# Limita ingreso
def limites(frase,minimo,maximo):    
    flag=True
    while flag:
        y=validar_Dato(frase)
        if y<=maximo and y>=minimo:
            flag=False
        else:
            print(f'El dato ingresado esta por fuera de los limites establecidos min {minimo} y max {maximo}')

    return y
# Calcula Matriz Moore- Penrose
def MooPen(x,te,t):
     if x==0:
          y_true=te[0]
     elif x == 1:
          y_true = te[1]*t+te[0]
     elif x == 2:
          y_true = (te[2]*(t**2)+te[1]*t+te[0])
     elif x ==3:
          y_true = (te[3]*(t**3)+te[2]*(t**2)+te[1]*t+te[0])
     elif x == 4:
          y_true = (te[4]*(t**4)+ te[3]*(t**3)+te[2]*(t**2)+te[1]*t+te[0])
     elif x == 5:
          y_true = (te[5]*(t**5)+te[4]*(t**4)+ te[3]*(t**3)+te[2]*(t**2)+te[1]*t+te[0])
     elif x == 6:
          y_true = (te[6]*(t**6)+te[5]*(t**5)+te[4]*(t**4)+ te[3]*(t**3)+te[2]*(t**2)+te[1]*t+te[0])
     
     return(y_true)
# Calcula Phi
def Phi(x,data):
     if x== 0:
          phi= np.array(data.ones).transpose()
     elif x == 1:
          phi = np.array([data.ones, data.t]).transpose()
     elif x == 2:
          phi = np.array([data.ones, data.t, data.t**2]).transpose()
     elif x == 3:
          phi = np.array([data.ones, data.t, data.t**2, data.t**3]).transpose()
     elif x == 4:
          phi = np.array([data.ones, data.t, data.t**2, data.t**3, data.t**4]).transpose()
     elif x==5:
          phi = np.array([data.ones, data.t, data.t**2, data.t**3, data.t**4,data.t**5]).transpose()    
     elif x==6:
          phi = np.array([data.ones, data.t, data.t**2, data.t**3, data.t**4,data.t**5, data.t**6]).transpose()    
     
     return(phi)
# Calcula Estimadores
def Estimados(x,theta,t):
     if x == 1:
          y_e = theta[1]*t+theta[0] 
     elif x == 2:
          y_e = (theta[2]*(t**2)+theta[1]*t+theta[0])
     elif x ==3:
          y_e = (theta[3]*(t**3)+theta[2]*(t**2)+theta[1]*t+theta[0])
     elif x==4:
          y_e = (theta[4]*(t**4)+theta[3]*(t**3)+theta[2]*(t**2)+theta[1]*t+theta[0])
     elif x==5:
          y_e = (theta[5]*(t**5)+theta[4]*(t**4)+theta[3]*(t**3)+theta[2]*(t**2)+theta[1]*t+theta[0])
     elif x==6:
          y_e = (theta[6]*(t**6)+theta[5]*(t**5)+theta[4]*(t**4)+theta[3]*(t**3)+theta[2]*(t**2)+theta[1]*t+theta[0])

     return(y_e)



flag1=True
while(flag1==1):

     ## Pido Orden de Polinomio
     x=limites('\nPorfavor ingrese el orden de modelo que desea (1-6): ',1,6)
     N=10
     t = np.linspace(0,10,N)
     te=[]

     ## Pido Valores de Theta
     for i in range(x+1):
          te.append(float(input(f"Porfavor ingrese valor de theta {i}: ")))

     ## Calculando la matriz Moore - Penrose
     y_true= MooPen(x,te,t)

     ## Señal de error de media 0:
     e = np.random.normal(0,0.1,size=N)

     ## Señal con error incluido
     y = y_true + e

     ## Creo DataFrame
     data = pd.DataFrame(data = {'t':t,'y':y})
     data['ones'] = 1
     data['y_true'] = y_true

     ## Calculo Phi
     phi=Phi(x,data)
     A = np.dot(phi.transpose(),phi)    
     Mpr = np.linalg.inv(A)

     ## Calculo Matriz de Estimadores
     B = np.dot(phi.transpose(),y)
     theta = np.dot(Mpr,B)

     ## Calculando los Datos de Salida con los Parámetros Estimados
     y_e=Estimados(x,theta,t)

     ## Grafica 
     plt.figure(figsize=(8,4))
     plt.plot(t,y_true)
     plt.scatter(t,y)
     plt.plot(t,y_e)
     plt.legend(["Ideal","Medición","Estimado"])
     plt.grid()
     print(f"\nVector Theta: {te}\n")
     print(f"Valores Esimados: {theta}")
     time.sleep(2)
     plt.show()