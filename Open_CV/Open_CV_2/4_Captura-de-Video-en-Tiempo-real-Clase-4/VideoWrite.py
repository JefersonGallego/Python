# Importar librerias
import cv2

# Capturar Camara
cap = cv2.VideoCapture(0)
# Dimensiones del video para guardarlo
ancho = int(cap.get(3)) 
alto = int(cap.get(4))

print(ancho, alto)

# cv2.VideoWriter(Nombre, Codificacion(Formato), FPS, Tamaño)cv2.VideoWriter_fourcc(*'MP4V')
fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter('Video4.mp4',fourcc , 10, (ancho, alto))

# Creamos un ciclo para ejecutar nuestros Frames
while True:
    # Leer fotogramas
    ret, frame = cap.read()

    # Guarda el video
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    # Mostramos los Frames
    cv2.imshow("VIDEO CAPTURA", frame)

    # Cerramos con lectura de teclado
    t = cv2.waitKey(1)
    if t == 27:
        break

# Liberamos la VideoCaptura
cap.release()
# Cerramos la ventana
cv2.destroyAllWindows()