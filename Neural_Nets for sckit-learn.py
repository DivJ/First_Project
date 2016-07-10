
# coding: utf-8

# In[3]:

from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
import numpy as np
from keras.utils import np_utils
from keras.layers import Dense,Activation
from keras.models import Sequential
get_ipython().magic(u'matplotlib inline')
digits=load_digits() 


# In[8]:

x_data=[]
for i in range(1797):
    x_data.append(digits.images[i].flatten())
x_data=np.asarray(x_data)


# In[9]:

labels=digits.target
labels=np.asarray(labels).reshape(1797,1)
labels=np_utils.to_categorical(labels,10)


# In[79]:

model=Sequential()
model.add(Dense(64,input_dim=64))
model.add(Activation('tanh'))
model.add(Dense(32))
model.add(Activation('tanh'))
model.add(Dense(16))
model.add(Activation('tanh'))
model.add(Dense(10))
model.add(Activation('tanh'))


# In[80]:

model.compile(optimizer='adadelta',loss='binary_crossentropy')


# In[81]:

model.fit(x_data[:1500,:],labels[:1500,:],nb_epoch=10,batch_size=50,shuffle=True,
          validation_data=(x_data[1500:,:],labels[1500:,:]))


# In[82]:

count=0
for i in range(10):
    tar=digits.target[i]
    url=digits.images[i]
    url=url.flatten()
    url=url.reshape(1,64)
    a=model.predict_classes(url)
    if a==tar:
        count+=1
print count

