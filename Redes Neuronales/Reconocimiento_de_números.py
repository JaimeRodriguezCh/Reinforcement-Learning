import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Cargar el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocesar los datos
train_images = train_images / 255.0
test_images = test_images / 255.0

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Crear el modelo de la red neuronal
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Aplanar la matriz de imágenes
    Dense(128, activation='relu'),  # Capa oculta con activación ReLU
    Dense(10, activation='softmax')  # Capa de salida con activación Softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar la red neuronal
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2)

# Evaluar la precisión en el conjunto de prueba
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print(f'Precisión en el conjunto de prueba: {test_accuracy * 100:.2f}%')