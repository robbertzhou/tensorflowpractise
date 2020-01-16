import tensorflow as tf
import tempfile

# tf.compat.v1.disable_eager_execution()
# # # hello = tf.constant("Hello")
# # # with tf.compat.v1.Session() as sess:
# # #     print(sess.run(hello))
import os # 运维模块， 调用系统命令
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 只显示warring和error

tf.compat.v1.disable_eager_execution()
a = tf.constant(5,name="a",dtype=tf.int16)
b = tf.constant(3,name="b",dtype=tf.int16)
c = tf.multiply(a,b,name="c")
d = tf.add(a,b,name="d")
e = tf.add(c,d,name="sum")


writer = tf.summary.create_file_writer('logs/')


with tf.compat.v1.Session() as sess:
    print("result is:" , sess.run(e))

