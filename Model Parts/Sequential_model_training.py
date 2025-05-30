#sequential model
model = Sequential()

#add input and h layers
model.add(Dense(128, input_shape=(784,), activation='relu'))
model.add(Dropout(0.2))
#add input ReLU activation
model.add(Dense(64, activation='relu'))

#add output layer
model.add(Dense(10, activation='softmax')) #10 classes

#compile model
model.compile(
    optimizer=Adam(learning_rate=0.001), 
    loss=categorical_crossentropy(),
    metrics=['accuracy']
)
#load mnist data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#reshape data
x_train=x_train.reshape(-1, 784).astype('float32')/255.0
x_test=x_test.reshape(-1, 784).astype('float32')/255.0

#one-hot encode labels
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

#train model
hstory=model.fit(
    x_train, y_train, 
    batch_size=32, 
    epochs=5, 
    validation_split=0.2, 
    verbose=1
)

