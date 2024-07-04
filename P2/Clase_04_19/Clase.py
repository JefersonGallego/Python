ano = int(input('¿Cúal años quiere saber si es bisisesto '))
if ano%4 == 0 and ano%100 == 0 and ano%400 == 0:
    print(f'El año de {ano} es bisiesto')
elif ano%4 == 0 and ano%100 != 0:
    print(f'El año {ano} es bisiesto')
else :
    print(f'El año {ano} no es bisiesto')