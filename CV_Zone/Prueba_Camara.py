import cv2

# Función para verificar si una resolución es soportada
def is_resolution_supported(cap, width, height):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    return actual_width == width and actual_height == height

# Iniciar captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Lista de resoluciones comunes
resolutions = [
    (640, 480),    # VGA
    (800, 600),    # SVGA
    (1024, 768),   # XGA
    (1280, 720),   # HD
    (1280, 1024),  # SXGA
    (1600, 1200),  # UXGA
    (1920, 1080),  # Full HD
    (2560, 1440),  # QHD
    (3840, 2160),  # 4K
]

# Probar cada resolución
supported_resolutions = []
for width, height in resolutions:
    if is_resolution_supported(cap, width, height):
        supported_resolutions.append((width, height))

# Liberar la captura de video
cap.release()

# Mostrar resoluciones soportadas
print("Resoluciones soportadas por la cámara:")
for resolution in supported_resolutions:
    print(f"{resolution[0]}x{resolution[1]}")

if not supported_resolutions:
    print("No se encontraron resoluciones soportadas.")
