from tensorflow.keras import models
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import cv2
import argparse
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("model", type=str, help="model.h5")
    parser.add_argument("--model", type=str, help="Name of the model.h5 in the model folder", default="image_classifier_model_v2")
    
    args = parser.parse_args()

    global model_name
     
    model_name = args.model
    
    print(f"model: {model_name}")

if __name__ == "__main__":
    main()

model_path = f'./model/{model_name}.h5'

model = models.load_model(model_path, custom_objects={'preprocess_input': preprocess_input, 'mse': 'mse'})

print(model.summary())

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Erro ao abrir a câmera.")
    exit()

ret, frame = cam.read()
if not ret:
    print("Erro ao capturar a imagem.")

# frame = cv2.imread(r"D:\Main dataset\Main dataset\4-Powdery Mildew\2.jpg", cv2.IMREAD_COLOR)

img = cv2.resize(frame, (224, 224))        

img = np.expand_dims(img, axis=0)

prediction = model.predict(img)

cam.release()

predicted_class = np.argmax(prediction)

print(prediction)

print(f'Classe prevista: {predicted_class}')

cv2.imshow(str(predicted_class), frame)

cv2.waitKey(0)

cv2.destroyAllWindows()