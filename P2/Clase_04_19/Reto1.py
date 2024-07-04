# Factorrial
num=int(input('Digite un Numero:'))
fac=1
print(f'{num}! = ',end=' ')

while num>0:
    if num>1:
        print(f'{num} x ',end=' ')
    else:
        print(f'{num} = ',end=' ')

    fac=fac*num
    num=num-1
print(fac)