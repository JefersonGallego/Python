# formula general Fibonacci = an = a(n-1) + a(n-2)

n1 = int(input('Digite el número de comienzo: '))
n2 = int(input('Digite el número que le sigue: '))
n3 = int(input('Digite el número de elementos de la secuencia: '))

print(f'\nSecuencia Fibonacci\n\n\t{n1}\n\t{n2}')

for i in range(0,n3+1):
    an = n1 + n2
    print(f'\t{an}')

# se actualizan los valores de a(n-1) y a(n-2)

    n1 = n2
    n2 = an

print('\ntermina ciclo\n')