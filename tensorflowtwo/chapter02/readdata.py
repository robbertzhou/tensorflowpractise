#coding:utf-8

import numpy as np
import tensorflow as tf
#step 1 读取数据
arr_list = np.arange(0,100).astype(np.float32)
shape = arr_list.shape
#step 2 使用dataset API读取数据
dataset = tf.data.Dataset.from_tensor_slices(arr_list)
dataset_iterator = dataset.shuffle(shape[0]).batch(10)

def model(xs):
    outputs = tf.multiply(xs,0.1)
    return outputs

for it in dataset_iterator:
    logits = model(it)
    print(logits.numpy())

