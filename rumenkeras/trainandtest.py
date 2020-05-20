import numpy as np
import rumenkeras.buildmodel as model
import tensorflow as tf
model.model.compile(optimizer='rmsprop',loss='mse',metrics='accuracy')
train_number = 100
train_data = np.random.random((train_number,2))
# print(train_data)
labels = [(1 if data[0] < data[1] else 0) for data in train_data]
model.model.fit(train_data,labels,epochs=20,batch_size=32)


test_number = 100
test_data = np.random.random((test_number,2))
expected = [(1 if data[0] < data[1] else 0) for data in test_data]
error = 0
for i in range(0,test_number):
    data = test_data[i].reshape(1,2)
    pred = 0 if model.model.predict(data) < 0.5 else 1
    if(pred!=expected[i]):
        error += 1

print("total errors:{},accuracy:{}".format(error,1.0 - error / test_number))