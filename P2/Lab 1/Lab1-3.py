# IMC

print('Hola, Porfavor digite los  siguientes datos:')
nombre = str(input('Digite su Nombre: '))
apellido = str(input('Digite su Apellido: '))
peso = float(input('Digite su Peso, en Libras: '))
altura = float(input('Digite su Altura, en Pies: '))

kg = peso*0.453592
m = altura*0.3048
imc = kg/(m)**2

print(f'Tu peso en kg es: {round(kg,2)}')
print(f'Tu Altura en m es: {round(m,2)}')
print(f'El Valor de tu IMC es: {round(imc,2)}')

if imc<=18.5:
    print(f'{nombre} {apellido} tienes un peso Bajo')

elif imc>18.5 and imc<=24.9: 
    print(f'{nombre} {apellido} tienes un peso Normal')

elif imc>24.9 and imc<=29.9: 
    print(f'{nombre} {apellido} tienes un Sobrepeso')

elif imc>29.9 and imc<=34.9:
    print(f'{nombre} {apellido} tienes Obesidad de Grado 1')

elif imc>34.9 and imc<=39.9:
    print(f'{nombre} {apellido} tienes Obesidad de Grado 2')

elif imc>39.9: 
    print(f'{nombre} {apellido} tienes Obesidad de Grado 3')
