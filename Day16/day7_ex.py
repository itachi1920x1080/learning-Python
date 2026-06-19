# pyrefly: ignore [missing-import]
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPool2D,Flatten,Dense,Dropout

(x_train,y_train),(x_test,y_test)=cifar10.load_data()

x_train = x_train.astype('float32')/255.0
x_test = x_test.astype('float32')/255.0

y_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)

print(f"Training Data Shape : {x_train.shape} ,{y_train.shape} ,{x_test.shape} ,{y_test.shape}")



model = Sequential([
    Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)),
    MaxPool2D((2,2)),
    Conv2D(64,(3,3),activation='relu'),
    MaxPool2D((2,2)),
    Flatten(),
    Dense(64,activation='relu'),
    Dropout(0.5),
    Dense(10,activation='softmax')
])

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

history = model.fit(x_train,y_train,epochs=10,batch_size=32,validation_split=0.1)

loss, accuracy = model.evaluate(x_test,y_test)
print(f"Test Accuracy: {accuracy:.4f}")



improved_model = Sequential([
    Conv2D(64,(3,3),activation="relu",input_shape=(32,32,3)),
    Conv2D(64,(3,3),activation='relu'),
    MaxPool2D((2,2)),
    Dropout(0.2),
    Conv2D(128,(3,3),activation="relu"),
    Conv2D(128,(3,3),activation='relu'),
    MaxPool2D((2,2)),
    Dropout(0.2),
    Flatten(),
    Dense(128,activation='relu'),
    Dropout(0.5),
    Dense(10,activation='softmax')
])


optimizer = tf.keras.optimizers.Adam(learning_rate = 0.001)

improved_model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

print("\nTraining Improved Model...")
improved_history = improved_model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

improved_loss, improved_accuracy = improved_model.evaluate(x_test, y_test)
print(f"Improved Test Accuracy: {improved_accuracy:.4f}")