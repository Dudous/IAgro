from tensorflow.keras import models
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input # já já tiro isso aqui
from generate_code import generateCode
import numpy as np
import argparse
import cv2
from datetime import datetime
import json
import time

classes = ['Healthy', 'Aphids', 'Target spot', 'Bacterial blight', 'Powdery mildew']

scan_body = {
    "DeviceId": generateCode(),
    "FieldId": "",
    "StartedAt": "",
    "CropDiseasesFound": []
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("field", type=str, help="Guid off the field")
    parser.add_argument("--model", type=str, help="Name of the model.h5 in the model folder", default="model_v1")
    
    global model_name

    args = parser.parse_args()
    
    model_name = args.model
    field_id = args.field
    startedAt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    scan_body["FieldId"] = field_id
    scan_body["StartedAt"] = startedAt

if __name__ == "__main__":
    main()

model_path = f'./model/{model_name}.h5'

model = models.load_model(model_path)

print(model.summary())


# with open('./scripts/data.json', 'r') as file:

#     coords = json.load(file)

#     for result in coords.keys():

#         lat, long = result.split(',')

#         crop_disease = {
#             "Disease": coords[result],
#             "DetectedAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
#             "LocationPoint": {
#                 "Latitude": lat, 
#                 "Longitude": long
#             }
#         }

#         scan_body["CropDiseasesFound"].append(crop_disease)

# scan_body = json.dumps(scan_body)

# with open('test.json', 'w') as file:
#     file.write(scan_body)

# frame = cv2.imread(r"D:\Main dataset\Main dataset\4-Powdery Mildew\2.jpg", cv2.IMREAD_COLOR)

cam = cv2.VideoCapture(0)

ret, frame = cam.read()

img = cv2.resize(frame, (224, 224))

img = np.expand_dims(img, axis=0)

prediction = model.predict(img)

prediction = np.argmax(prediction)

print(classes[prediction])


# cam = cv2.VideoCapture(0)

# if not cam.isOpened():
#     print("Erro ao abrir a câmera.")
#     exit()

# count = 1

# while 1:

#     count += 1

#     ret, frame = cam.read()

#     if not ret:
#         print("Erro ao capturar a imagem.")

#     img = cv2.resize(frame, (224, 224))

#     img = np.expand_dims(img, axis=0)

#     prediction = model.predict(img)

#     # predicted_class = np.argmax(prediction)
#     cv2.putText(frame, str(count), (10, 100), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (0,0,0))

#     cv2.imshow("Pressione 'Esc' para finalizar", frame)

#     key = cv2.waitKey(1)

#     if key == 27:  # Esc para sair
#         break

#     # print(prediction)

# cam.release()
# cv2.destroyAllWindows()
