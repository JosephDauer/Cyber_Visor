import tensorflow as tf

#ReLU standard
x = tf.nn.relu(inputs)

#leaky ReLU with alpha
x = tf.nn.leaky_relu(inputs, alpha=0.2)

#swich activation
x = tf.nn.swish(inputs)

