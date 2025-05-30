import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model

#define encoder
input_dim = 784 #
encoding_dim = 64

input_layer = Input(shape=(input_dim,))
encoder = Dense(encoding_dim, activation='relu')(input_layer)

bottleneck = Dense(encoding_dim // 2,
activation='relu')(encoder)

#define decoder
decoder = Dense(encoding_dim,activation='relu')(bottleneck)
output_layer = Dense(input_dim, activation='sigmoid')(decoder)

#autoencoder model
autoencoder = Model(inputs=input_layer, outputs=output_layer)
autoencoder.compile(optimizer='adam', loss='mse') #research compilers tools

#summary of model
autoencoder.summary()
