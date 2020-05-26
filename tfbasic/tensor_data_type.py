#coding:utf-8
#tensorflow数据类型
import tensorflow as tf
import numpy as np

with tf.device('cpu'):
    a = tf.constant([1])
with tf.device('gpu'):
    b = tf.constant([1])

tf.compat.v1.disable_eager_execution()
sess = tf.compat.v1.Session()
#数据类型转换
a = np.arange(5)
print(a)
aa = tf.convert_to_tensor(a,dtype=tf.int32) # numpy转tensor
print(sess.run(aa))

tf.cast(aa,dtype=tf.float32)  # tensor之间数据类型转换


# int --》 bool
b = tf.constant([0,1])
tf.cast(b,dtype=tf.bool) # int --》bool

# tf.Variable
a = tf.range(5)
b = tf.Variable(a) # tensor转为Variable后具有求导的特性，即自动记录a的梯度相关信息
b.name # Variable:0

b = tf.Variable(a, name='input_data')
b.name # input_data:0
b.trainable # True

isinstance(b,tf.Tensor)  # False
isinstance(b,tf.Variable)  # True
tf.is_tensor(b)  # True  # 推荐使用


a= tf.range(5)
a.numpy()

# a必须是scalar
a = tf.ones([])
a.numpy()
int(a)
float(a)