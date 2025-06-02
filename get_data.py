# from tensorflow.keras import models
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input # já já tiro isso aqui
from Generate_Code import generateCode
import numpy as np
import argparse
import cv2
from datetime import datetime
import json

classes = ['Healthy', 'Aphids', 'Target spot', 'Bacterial blight', 'Powdery mildew',]

scan_body = {
    "DeviceId": generateCode(),
    "FieldId": "",
    "CropDiseases": []
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("field", type=str, help="Guid off the field")
    parser.add_argument("--model", type=str, help="Name of the model.h5 in the model folder", default="image_classifier_model_v2")
    
    global model_name

    args = parser.parse_args()
    
    model_name = args.model
    field_id = args.field

    scan_body["FieldId"] = field_id

if __name__ == "__main__":
    main()

model_path = f'./model/{model_name}.h5'

# model = models.load_model(model_path, custom_objects={'preprocess_input': preprocess_input, 'mse': 'mse'})

# print(model.summary())


with open('data.json', 'r') as file:

    coords = json.load(file)

    # LOOP PRINCIPAL
    for result in coords.keys():

        lat, long = result.split(',')

        crop_disease = {
            "Disease": coords[result],
            "DetectedAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "LocationPoint": {
                "Latitude": lat,
                "Longitude": long
            }
        }

        scan_body["CropDiseases"].append(crop_disease)

scan_body = json.dumps(scan_body)

print(scan_body)


# frame = cv2.imread(r"D:\Main dataset\Main dataset\4-Powdery Mildew\2.jpg", cv2.IMREAD_COLOR)

# cam = cv2.VideoCapture(0)

# if not cam.isOpened():
#     print("Erro ao abrir a câmera.")
#     exit()

# ret, frame = cam.read()

# if not ret:
#     print("Erro ao capturar a imagem.")

# img = cv2.resize(frame, (224, 224))

# img = np.expand_dims(img, axis=0)

# prediction = model.predict(img)

# predicted_class = np.argmax(prediction)

# print(prediction)

# cam.release()