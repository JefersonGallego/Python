# Importamos las librerias
import cv2
import matplotlib.pyplot as plt


# Imagen
# Vamos a crear nuestra matriz (Canal) principal
img = cv2.imread("goo.png")
# Corregcion BGR a RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(img)

# Extraccion de 3 Canales Comando
R,G,B = cv2.split(img)

# Mostramos nuestros canales
fig = plt.figure()
# C1 RED
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(R, cmap="gray")
ax1.set_title("Channel Red")
# C2 GREEN
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(G, cmap="gray")
ax2.set_title("Channel Green ")
# C3 BLUE
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(B, cmap="gray")
ax3.set_title("Channel Blue")

# RECONSTRUCCION
imgre = cv2.merge((R,G,B))

# IMAGEN ORIGINAL
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(imgre)
ax4.set_title("Image Original")
#plt.imshow(img)

plt.show()

# Con el teclado pasamos la imagen
cv2.waitKey(0)