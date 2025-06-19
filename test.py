from tensorflow.keras import models
import numpy as np
import cv2

classes = ['Healthy', 'Aphids', 'Target spot', 'Bacterial blight', 'Powdery mildew']

model_path = f'./model/model_v1.h5'

model = models.load_model(model_path)

print(model.summary())

cam = cv2.VideoCapture(0)

ret, frame = cam.read()

img = cv2.resize(frame, (224, 224))

img = np.expand_dims(img, axis=0)

prediction = model.predict(img)

prediction = np.argmax(prediction)

print(classes[prediction])