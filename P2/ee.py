import numpy as np
import math as mt
import matplotlib.pyplot as pt

x= np.arange (0,10,0.1) # Datos en x
y=2*np.sin(x) # Datos en y

pt.plot(x, y,)

# Texto en la gráfica en coordenadas (x,y)
texto1 = pt.text(3,4, r'$\frac{\sin(x)}{x}$', fontsize=20)

# Punto a señalar en la primera gráfica
px =1
py=2
# Pinto las coordenadas con un punto negro
punto = pt.plot([px],[py], 'bo')

# Hago un señalización con flecha
nota = pt.annotate(r'$\frac{\sin(7.5)}{\exp(-7.5)} = 0.12$',
         xy=(px, py),
         xycoords='data',
         xytext=(px,py),
         fontsize=9)

pt.grid()  # Malla

pt.title('Representacion de dos funciones')
pt.xlabel('Tiempo / s')
pt.ylabel('Amplitud / cm')

pt.show()

