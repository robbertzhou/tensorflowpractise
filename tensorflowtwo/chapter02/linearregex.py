import tensorflow as tf

weight = tf.Variable(1.0,name="weight")
bias = tf.Variable(1.0,name="bias")

def model(xs):
    logits = tf.multiply(xs,weight) + bias
    return logits

