from sklearn.model_selection import GridSearchCV
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense 
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier

#Define a simple Keras model
def create_model(learning_rate=0.01):
    model = Sequential([
        Dense(64, input_dim=20, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

# Wrap model scikit-learn compatbility
model =KerasClassifier(build_fn=create_model, epochs=10, batch_size=32)

# Define the grid search parameters
param_grid = {
    'learning_rate': [0.001, 0.01. 0.1],
    'batch_size': [16, 32, 64],
}

#Perform grid search
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring='accuracy', cv=3)
grid_result = grid.fit(X_train, y_train)

print(f"Best: {grid_result.best_score_} using {grid_result.best_params_}")

