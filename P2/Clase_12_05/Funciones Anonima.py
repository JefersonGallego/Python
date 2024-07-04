from calendar import c


def suma(a,b):
    c=a+b
    return c

def suma(a,b):
    return a+b

#Lamba Funcion

suma_lambda = lambda a,b: a+b


print(suma(5,4))
print(suma_lambda(5,4))      # Siempre y cuanndo necesitemos returnan un solo 

#------------------------------------------------------------------------------------------------

# Funcion Lambda para disriminante 

discriminante= lambda a,b,c: b**2 - 4*a*c

print(discriminante(1,2,2))
