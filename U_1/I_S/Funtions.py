import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import *
import math as ma

def crammer(mat,vec):
    d = np.linalg.det(mat)
    
    mat1= np.array([vec,mat[:,1],mat[:,2]])
    mat2= np.array([mat[:,0],vec,mat[:,2]])
    mat3= np.array([mat[:,0],mat[:,1],vec])
    
    d1 = np.linalg.det(mat1)
    d2 = np.linalg.det(mat2)
    d3 = np.linalg.det(mat3)
    
    x1 =d1/d
    x2 =d2/d
    x3= d3/d
    
    return x1,x2,x3

def crammer_2(mat,vec):
    d = np.linalg.det(mat)
    
    mat1= np.array([vec,mat[:,1]])
    mat2= np.array([mat[:,0],vec])
    
    d1 = np.linalg.det(mat1)
    d2 = np.linalg.det(mat2)
    
    x1 =d1/d
    x2 =d2/d

    return x1,x2


"""
##Example
matrix_l = np.array([[8,4,6],
                   [5,0,6],
                   [2,4,3]])

vector_a = np.array([9,8,5])

matrix_2 = np.array([[-0.5,3.5],
                   [6.8,5]])

vector_b = np.array([0.52,6])

print(crammer(matrix_l,vector_a))
print(crammer_2(matrix_2,vector_b))

"""

# Error
def error (actual, pred):
    actual, pred = np.array (actual), np.array (pred)
    return abs(np.subtract(actual, pred)). mean () 
"""
##Example
x = [12, 13, 14, 15, 15, 22, 27]
y = [11, 13, 14, 14, 15, 16, 18]

a =error(x,y)
print(a)
"""

# MSE
def mse (actual, pred):
    actul, pred = np.array (actual), np.array (pred)
    a = np.square (np.subtract (actual, pred)). mean () 
    return a

"""
##Example
x = [12, 13, 14, 15, 15, 22, 27]
y = [11, 13, 14, 14, 15, 16, 18]

a =mse(x,y)
print(a)
"""

# Interpolation
def interpolation(x, y,a):
    y_interp = interp1d(x,y)
    return y_interp(a)
"""
##Example

x = [1.504,1.634] 
y = [0.56,.63]

a=1.5775
 
print(f" {a} in {x},{y} is",
             interpolation(x,y,a))
"""
# Validar Datos
def validar_Dato(frase):

    while True:
            valor= input(frase)     
            if valor.isnumeric():
                valor = int(valor)
                break
            else:
                print('El dato ingresado no es numerico , por favor ingresar un dato numerico')

    return valor

def limites(frase,minimo,maximo):    
    flag=True
    while flag:
        y=validar_Dato(frase)
        if y<=maximo and y>=minimo:
            flag=False
        else:
            print(f'El dato ingresado esta por fuera de los limites establecidos min {minimo} y max {maximo}')

    return y

# Integrals
def integrand(x, a):
    return a*x

def integrand_1(x,a):
    return (a)*(x)**2

def expint(x):
    return abs(quad(integrand, 0, np.inf, args=(x))[0])

def expint_1(x):
    return abs(quad(integrand_1, 0, np.inf, args=(x))[0])

