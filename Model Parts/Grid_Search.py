from sklearn.model_selection import GridSearchCV
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import control_dependencies
from tensorflow.keras.wrappers.scikit_learn import Keras Classifier

#defining keras model
def create_model(learning_rate=o.1):
    modelsequential([
        Dense(64, input_dim=20, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='binary_crossentropy',
                  metrics='accuracy')
    return model
)
Model = kerasclassifier(build_fn=create_model, epochs=100, batch_size=12)

param_grid = {
    'batch_size': [16, 32, 64],
    'epochs': [10, 50, 100],
    'learning_rate': [0.01, 0.1, 0.2]
}
grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring='accuracy', cv=3)
grid_result = grid.fit(x_train, y_train)

print("Best:{grid_result.best_score_} using {grid_result.best_params_}")
