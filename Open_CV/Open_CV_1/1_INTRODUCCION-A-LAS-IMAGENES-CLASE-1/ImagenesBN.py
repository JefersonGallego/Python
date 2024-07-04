# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Imagen Negra
# Vamos a crear nuestra imagen negra
img = 255*np.ones((10,10,1), np.uint8) # Matriz 10x10x 1 Canal 

# Creo Pixeles  [Filas, Columnas]
img[0,1] = 25
img[2,3] = 50
img[4,5] = 150
img[6,7] = 200

# Mostramos los valores numericos
print(img)
# Mostramos nuestra imagen
plt.title(" Image Representation in Numerical Data ",fontsize = 14)
plt.imshow(img, cmap='Blues')
plt.ylabel(' Rows ', fontsize = 14)
plt.xlabel(' Columns', fontsize = 14)
plt.show()

