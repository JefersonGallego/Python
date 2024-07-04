# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Imagen
# Vamos a crear nuestra matriz principal
img = np.ones((1,1,3), np.uint8) # Matriz 1x1x 3 Canales 

# Extraemos los canales
R = img[:,:,0] # Canal 1 Matriz 1x1
G = img[:,:,1] # Canal 2 Matriz 1x1
B = img[:,:,2] # Canal 3 Matriz 1x1

# Modificamos canales
R[:,:] = 0
G[:,:] = 0
B[:,:] = 0
print(R,G,B)
# Modificamos l imagen
img[:,:,0] = R
img[:,:,1] = G
img[:,:,2] = B

print(img)


# Mostramos nuestra imagen
plt.imshow(img)
plt.show()

# Con el teclado pasamos la imagen
cv2.waitKey(0)