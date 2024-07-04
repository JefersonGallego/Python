#Ejemplo Tuplas

n = int(input('¿Cuantos numeros enteros quiere verificar?'))
numeros = []

for i in range(n):
    signo = ""
    num = int(input('Digite el Numero:'))
    if num > 0:
        signo = 'Postivo'
    elif num == 0:
        signo= 'Cero'
    else:
        signo = 'Negativo'
    numeros.append((num,signo))

    print(numeros)