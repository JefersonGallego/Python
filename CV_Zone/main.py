import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import cv2
from cvzone.HandTrackingModule import HandDetector

# Inicializa la captura de video desde la cámara web
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Configura la resolución del video
video.set(3, 1280)
video.set(4, 720)

# Inicializa el detector de manos
detector = HandDetector()
# Lista para almacenar los puntos donde se dibujará
desenho = []

while True:
    # Captura un fotograma del video
    check, img = video.read()
    # Detecta manos en el fotograma y dibuja las manos encontradas
    resultado = detector.findHands(img, draw=True)
    # Obtiene la primera mano detectada
    hand = resultado[0]

    if hand:
        # Obtiene la lista de puntos de referencia de la mano
        lmlist = hand[0]['lmList']
        # Verifica cuáles dedos están levantados
        dedos = detector.fingersUp(hand[0])
        # Cuenta el número de dedos levantados
        dedosLev = dedos.count(1)

        # Si hay un dedo levantado (índice), dibuja un círculo y añade el punto a la lista
        if dedosLev == 1:
            x, y = lmlist[8][0], lmlist[8][1]
            cv2.circle(img, (x, y), 15, (0, 0, 255), cv2.FILLED)
            desenho.append((x, y))
        # Si no hay exactamente un dedo o tres dedos levantados, añade un punto de pausa
        elif dedosLev != 3:
            desenho.append((0, 0))
        # Si hay tres dedos levantados, limpia el dibujo
        elif dedosLev == 3:
            desenho = []

        # Dibuja círculos y líneas basados en los puntos almacenados en desenho
        for id, ponto in enumerate(desenho):
            x, y = ponto
            if x != 0:
                cv2.circle(img, (x, y), 10, (0, 0, 255), cv2.FILLED)
            if id >= 1:
                ax, ay = desenho[id - 1]
                if x != 0 and ax != 0:
                    cv2.line(img, (x, y), (ax, ay), (0, 0, 255), 20)

    # Voltea la imagen horizontalmente para una vista en espejo
    imgFlip = cv2.flip(img, 1)
    # Muestra la imagen en una ventana
    cv2.imshow('Img', imgFlip)
    # Si se presiona la tecla 'Esc', sale del bucle
    if cv2.waitKey(1) == 27:
        break

# Libera la cámara y cierra las ventanas
video.release()
cv2.destroyAllWindows()

