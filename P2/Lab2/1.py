from contextlib import ContextDecorator
from operator import truediv



conteo=0
suma=0

while True:
    num= input('Digite un Numero:') 
    num = num.strip()    # Corre espacios
    
    if num.isnumeric() == True:   # Num es Numerico?
        
         suma += int(num)
         conteo += 1
         media= suma / conteo
    elif num[:3].lower() =='fin':
         break
else:
         print('El Numero no es Valido')

print(f'El Sumatorio es de: {suma}')
print(f'La Cantidad de Numeros es: {conteo}')
print(f'La media es de {media}')



