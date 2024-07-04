import serial 
import numpy  as np


dato = serial.Serial('COM3',115200)  # Abre puerto serial @ 155200 bauds:

comando= 't'             #Comando de Control

comando=str.encode('t')  # Conversion Str a Byte

dato.write(comando)      # Transferencia de Comando

#tm=dato.readline()      # 
tm=2200
tm=float(tm)




print (valor_pertenencia)
print('Hola Mundo')