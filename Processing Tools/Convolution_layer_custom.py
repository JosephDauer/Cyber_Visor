import tensorflow as tf

class CustomConvlayer(tf.keras.layers.Layer):
    def __init__(self, filters, kernel_size):
        super(CustomConvLayer, self).__init__()
        self.conv = tf.keras.layers.conv2D(filters, kernel_size, padding='same')
        self.bn = tf.keras.layers.BatchNormalization()

    def call(self, inputs, training=False):
        x = self.conv(inputs)
        x = self.bn(x, training=training)
        return tf.nn.relux(x)
    