import os
import random
import glob
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import tensorflow as tf
from tensorflow.keras import models, layers, activations, optimizers, utils, losses, initializers, metrics, callbacks, preprocessing
from sklearn.model_selection import train_test_split

epochs = 100
batch_size = 32
patience = 5
learning_rate = 0.001
model_path = 'checkpoints/model.keras'

# Carrega modelo se já existir um checkpoint, caso contrário, o cria.
model = models.Sequential([
    layers.Resizing(56, 56),
    layers.Rescaling(1.0/255),
    layers.RandomRotation((-0.2, 0.2)),
    layers.Conv2D(32, (3, 3),
    activation = 'relu',
    kernel_initializer = initializers.RandomNormal()
    ),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3),
    activation = 'relu',
    kernel_initializer = initializers.RandomNormal()
    ),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dropout(0.5),
    layers.Dense(128,
    activation = 'relu',
    kernel_initializer = initializers.RandomNormal()
    ),
    layers.Dense(64,
    activation = 'relu',
    kernel_initializer = initializers.RandomNormal()
    ),
    layers.Dense(64,
    activation = 'relu',
    kernel_initializer = initializers.RandomNormal()
    ),
    layers.Dense(1,
    activation = 'sigmoid',
    kernel_initializer = initializers.RandomNormal()
    )
])

model.compile(
    optimizer = optimizers.Adam(
        learning_rate = learning_rate
    ),
    loss = losses.BinaryCrossentropy(),
    metrics = [ metrics.BinaryAccuracy(), metrics.CategoricalAccuracy() ]
)

IMG_SIZE = 160
BATCH_SIZE = 32
FILE_PATH = r'C:\Users\eduar\OneDrive\Desktop\Repos\IAgro\project\dataset\Cotton leaves\40 Images'
CLASSES = os.listdir(FILE_PATH)
SEED = 123  

# Training dataset
train_ds = utils.image_dataset_from_directory(
    FILE_PATH,
    validation_split=0.2,
    subset="training",
    seed=SEED,
    label_mode='int',
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    interpolation='nearest',
    class_names=CLASSES,
    shuffle=True
)

# Validation (test) dataset
val_ds = tf.keras.utils.image_dataset_from_directory(
    FILE_PATH,
    validation_split=0.2,
    subset="validation",
    seed=SEED,
    label_mode='int',
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    interpolation='nearest',
    class_names=CLASSES,
    shuffle=True
)


# %%
model.fit(train_ds,
    epochs = epochs,
    validation_data = val_ds,
    callbacks= [
        callbacks.EarlyStopping(
        monitor = 'val_loss',
        patience = patience,
        verbose = 1
        ),
        callbacks.ModelCheckpoint(
            filepath = model_path,
            save_weights_only = False,
            monitor = 'loss',
            mode = 'min',
            save_best_only = True
        )
    ]
)
