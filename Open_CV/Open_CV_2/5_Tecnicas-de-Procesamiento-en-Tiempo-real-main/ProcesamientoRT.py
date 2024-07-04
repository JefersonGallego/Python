import cv2
import numpy as np

# Parámetros para detector de esquinas
esquinas_param = dict(maxCorners=500, qualityLevel=0.2, minDistance=15, blockSize=9)
# Parámetros para detector de líneas
lineas_param = dict(rho=1, theta=np.pi / 180, threshold=100)
# Parámetros para detector de círculos
circulos_param = dict(method=cv2.HOUGH_GRADIENT, dp=1, minDist=30, param1=50, param2=30, minRadius=0, maxRadius=30)  

# Modo inicial: captura de video
mood = 48

# Crear la captura de video desde la cámara
cap = cv2.VideoCapture(1)

# Bucle principal para procesamiento de frames
while True:
    # Leer un frame de la captura de video
    ret, frame = cap.read()

    # Mostrar el modo actual
    modo_str = ""
    if mood == 48:
        modo_str = "Modo Normal"
        resultado = frame  # Modo normal
    elif mood == 49:
        modo_str = "Modo Desenfoque"
        resultado = cv2.blur(frame, (15, 15))  # Filtro de desenfoque
    elif mood == 51:
        modo_str = "Modo Bordes"
        resultado = cv2.Canny(frame, 100, 100)  # Detector de bordes
    elif mood == 50:
        modo_str = "Modo Esquinas"
        resultado = frame.copy()  # Copiar el frame original
        gray_esq = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        esquinas = cv2.goodFeaturesToTrack(gray_esq, **esquinas_param)
        if esquinas is not None:
            for x, y in np.float32(esquinas).reshape(-1, 2):
                cv2.circle(resultado, (int(x), int(y)), 5, (0, 0, 0), 2)  # Dibujar esquinas
    elif mood == 52:
        modo_str = "Modo Circulos"
        resultado = frame.copy()  
        gray_circ = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        circulos = cv2.HoughCircles(gray_circ, **circulos_param)
        if circulos is not None:
            circulos = np.uint16(np.around(circulos))
            for x, y, r in circulos[0, :]:
                cv2.circle(resultado, (x, y), r, (255, 255, 255), 2)  # Dibujar círculos
    elif mood == 53:
        modo_str = "Modo Lineas"
        resultado = frame.copy()  
        gray_lines = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_lines, 50, 150, apertureSize=3)
        lines = cv2.HoughLines(edges, **lineas_param)
        if lines is not None:
            for rho, theta in lines[:, 0]:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 500 * (-b))
                y1 = int(y0 + 500 * (a))
                x2 = int(x0 - 500 * (-b))
                y2 = int(y0 - 500 * (a))
                cv2.line(resultado, (x1, y1), (x2, y2), (0, 255, 0), 2) # Dibujar Lineas

    else:
        resultado = frame  # Modo por defecto si se presiona una tecla incorrecta
        modo_str = "Modo Desconocido"
        print('TECLA INCORRECTA')
        print()

    # Mostrar el modo actual en la parte superior del frame
    cv2.putText(resultado, modo_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Mostrar el frame procesado
    cv2.imshow("VIDEO CAPTURA", resultado)

    # Esperar por una tecla y actualizar el modo (mood)
    t = cv2.waitKey(1)
    if t == 27:  # Presionar ESC para salir
        break
    elif t != -1:
        mood = t

# Liberar la captura de video y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
