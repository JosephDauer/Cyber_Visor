import tensorflow as tf
from tensorflow.keras.models import sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
