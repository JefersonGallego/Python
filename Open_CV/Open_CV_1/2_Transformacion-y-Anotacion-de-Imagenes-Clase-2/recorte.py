# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Creamos imagen
# Vamos a crear nuestra matriz principal
img = 255 * np.ones((10,10,3), np.uint8)
img2 = 255 * np.ones((10,10,3), np.uint8)

# Modificamos los pixeles que vamos a extraer
# Img [Fila, Columna, Matriz]

# Modificamos Pixel Matriz R
img[4,5,0] = 255
img[4,4,0] = 0
img[5,4,0] = 255
img[5,5,0] = 0

# Modificamos Pixel Matriz G
img[4,5,1] = 0
img[4,4,1] = 255
img[5,4,1] = 0
img[5,5,1] = 255

# Modificamos Pixel Matriz B
img[4,5,2] = 255
img[4,4,2] = 255
img[5,4,2] = 0
img[5,5,2] = 0

# Realizamos recorte (filas, columnas)
recorte = img[3:7, 3:7]

# Mostramos nuestros canales
fig = plt.figure()
# imagen original
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img)
ax1.set_title("IMAGEN")
# recorte
ax2 = fig.add_subplot(1,2,2)
ax2.imshow(recorte)
ax2.set_title("RECORTE")
plt.show()

# Ahora con imagenes
# Leemos la img
imagen =cv2.imread('img.png')

# Truco paint
rct = imagen[8:30, 225:275]

# Mostramos el recorte
cv2.imshow('IMAGEN ORIGINAL', imagen)
cv2.imshow('RECORTE', rct)

cv2.waitKey(0)




