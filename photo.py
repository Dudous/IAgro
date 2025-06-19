import cv2
import time

# Inicializa a câmera
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

last_capture_time = time.time()

while True:
    ret, frame = cam.read()

    if not ret:
        print("Erro ao capturar a imagem.")
        break

    # Mostra o preview em tempo real
    cv2.imshow('Camera', frame)

    # Verifica se passou 1 segundo desde a última foto
    current_time = time.time()
    if current_time - last_capture_time >= 2:
        print('é os guri')
        last_capture_time = current_time

    # Se apertar ESC, sai
    if cv2.waitKey(1) == 27:
        break

# Encerra tudo
cam.release()
cv2.destroyAllWindows()
