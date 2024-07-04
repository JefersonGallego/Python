# Importamos librerias
import cv2

# aptura CamaraC
cap = cv2.VideoCapture(0) # cap = cv2.VideoCapture(0) Depende de cantidad de camaras

# Ciclo para captura de Imagenes
while True:
    # Leer fotogramas
    # ret = True / False si la captura es correcta o no
    # frame = Fotogramas
    ret, frame = cap.read()
    print(ret)
    # Mostrar Frame Tiempo Real
    cv2.imshow("VIDEO CAPTURA", frame)
    # Cerrar lectura
    t = cv2.waitKey(1) # Leer Teclado cada 1 mls
    if t == 27:        # t = 27 = Escape
        break

# Liberar VideoCaptura
cap.release()
# Cerrar Ventana
cv2.destroyAllWindows()