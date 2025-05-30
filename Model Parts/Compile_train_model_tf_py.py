#complile model
model.compile(optimizer='adam', loss=''categorical_crossentropy', metrics=['accuracy'])
              
#train model
history = model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_split=0.2)

optimize_model = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_function = tf.keras.losses.CategoricalCrossentropy()

#training loop (custom or not)
for epoch in range(5):
    with tf.GradientTape() as tape:
        predictions = model(X_train, training=True)
        loss = loss_function(y_train, predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply.gradients(zip(gradients, model.trainable_variables))

# situationally manual training loops
#importtorch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

#Train the model
for epoch in range(5):
    running_loss = 0.0
    for inputs, labels inn train_loader:
        optimizer.zerp_grad()
        outputs = model(inputs)
        loss = criterion(outputs, Labels)
        loss.backward()
        optimzer.step()
        running_loss += loss.item()

print(f'Epoch {epoch+1}, Loss: {running_loss/len(train_loader):.4f}')

