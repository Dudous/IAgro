from tensorflow.keras import models
from tensorflow.keras.preprocessing import image
import numpy as np

model_path = '../checkpoints/model.keras'

model = models.load_model(model_path)

img_path = r'C:\Users\eduar\OneDrive\Desktop\Repos\IAgro\project\dataset\Cotton leaves\40 Images\Healthy\10.jpg'

img = image.load_img(img_path, target_size=(160, 160))

predictions = model.predict(img)

predicted_class = np.argmax(predictions, axis=1)

class_names = ['Aphids', 'Army worm', 'Bacterial blight', 'Healthy', 'Powdery mildew', 'Target spot']

print(f'predicted: {class_names[predicted_class[0]]}')