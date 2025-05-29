import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing import image_dataset_from_directory

# === Diretório e parâmetros ===
data_dir = r'D:\Main dataset'  # substitua conforme necessário
img_size = (224, 224)
batch_size = 32
epochs_finetune = 5
total_epochs = 15

# === Data augmentation + normalização ===
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip('horizontal'),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
])

preprocessing = tf.keras.Sequential([
    layers.Rescaling(1./255),  # Normaliza para [0,1]
    layers.Lambda(preprocess_input)  # Aplica normalização do MobileNetV2
])

# === Carregar datasets ===
train_ds = image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='training',
    seed=42,
    image_size=img_size,
    batch_size=batch_size,
    label_mode='int'  # rótulo como inteiro
)

val_ds = image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='validation',
    seed=42,
    image_size=img_size,
    batch_size=batch_size,
    label_mode='int'
)

# === Normalizar rótulos para [0, 1] ===
def scale_labels(x, y):
    y = tf.cast(y, tf.float32) / 5.0  # Normaliza para [0,1]
    return x, y

train_ds = train_ds.map(scale_labels).prefetch(tf.data.AUTOTUNE)
val_ds = val_ds.map(scale_labels).prefetch(tf.data.AUTOTUNE)

# === Base model ===
base_model = MobileNetV2(
    input_shape=img_size + (3,),
    include_top=False,
    weights='imagenet')
base_model.trainable = False  # congela no começo

# === Modelo completo ===
model = models.Sequential([
    data_augmentation,
    preprocessing,
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.3),
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='linear')  # Previsão contínua
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# === Treinar etapa 1: base congelada ===
print("Treinando com base congelada...")
history = model.fit(train_ds, validation_data=val_ds, epochs=epochs_finetune)

# === Fine-tuning: destrava a base ===
print("Fine-tuning...")
base_model.trainable = True
model.compile(optimizer=tf.keras.optimizers.Adam(1e-5), loss='mse', metrics=['mae'])

history_finetune = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=total_epochs - epochs_finetune
)
