# conding:utf-8

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation
from tensorflow.keras.utils import plot_model
import pydot

#Dense(4)定义一个全连接层
#
model = Sequential([
    Dense(4,input_shape=(4,)),
    Activation('sigmoid'),
    Dense(1),
    Activation('sigmoid')
])

plot_model(model,to_file='training.png',show_shapes=True)

