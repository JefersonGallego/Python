import cv2
from cvzone.HandTrackingModule import HandDetector

# Inicializar la captura de video desde la cámara
video = cv2.VideoCapture(0)

# Verificar si la cámara se abrió correctamente
if not video.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

# Inicializar el detector de manos
detector = HandDetector(detectionCon=0.8, maxHands=2)

# Contador de imágenes guardadas
saved_image_counter = 0

try:
    while True:
        # Leer un cuadro de la cámara
        ret, img = video.read()
        if not ret:
            print("Error: No se pudo leer el cuadro de la cámara.")
            break

        # Detectar manos en el cuadro
        hands, img = detector.findHands(img, draw=True)

        # Mostrar el número de manos detectadas en tiempo real
        if hands:
            cv2.putText(img, f'Manos detectadas: {len(hands)}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # Dibujar las coordenadas (x, y) en la imagen
            for hand in hands:
                x, y, w, h = hand['bbox']
                cv2.putText(img, f'({x},{y})', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Mostrar la imagen con las manos detectadas
        cv2.imshow("Resultado: ", img)

        # Esperar por una tecla presionada
        key = cv2.waitKey(1)
        if key == 27:  # ESC para salir
            break
        elif key == ord('s'):  # 's' para guardar la imagen
            cv2.imwrite(f'mano_detectada_{saved_image_counter}.jpg', img)
            saved_image_counter += 1
            print(f'Imagen guardada como mano_detectada_{saved_image_counter}.jpg')

except Exception as e:
    print(f"Error: {e}")

finally:
    # Liberar la cámara y cerrar todas las ventanas
    video.release()
    cv2.destroyAllWindows()
