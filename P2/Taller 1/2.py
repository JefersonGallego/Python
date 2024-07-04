from cmath import asin, cos, sin, sqrt, pi
from math import degrees
from operator import truediv

while True:
    AB= int(input('Digite Cateto AB:'))  # Pido C1

    if AB>0 and AB<=100:  # El C1 esta entre 0 - 100 ?
          
         while True:
              BC= int(input('Digite Cateto BC:')) # Pido C2
              
              if BC>0 and BC<=100:  # El C2 esta entre 0 - 100 ?
                  
                   AC  =  sqrt(((AB)**2) + ((BC)**2))  # Hallo Hipotenusa
                   ACB= asin(AB/AC)                    # Hallo Angulo ACB
                   ACB = (ACB*180)/pi                  # Convierto a Grados ACB
                   BMC = 90                            # Punto medio M       
                   MBC= 180-BMC-ACB                    # Hallo MBC
                   MBC = abs(MBC)                      # Valor Absoluto para MBC
                   break                               # Rompe todo el Ciclo
              else:
               print('El Numero no es Valido') # Segundo Numero no Valido
         break                       
    else:
         print('El Numero no es Valido')       # Primer Numero no Valido

print(f'El Valor de tu Primer Cateto es : {AB}')
print(f'El Valor de tu Segundo Cateto es : {BC}')
print(f'El Valor de Teta es : {round(MBC,)}')