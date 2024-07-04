# Funcion de Orden Superior
from re import X


def math_opration(fun,x):
    return fun(x)
# Funciones
def product(a,b):
    return a*b
def cubed(a):
    return a**3

print(math_opration(cubed,2))

