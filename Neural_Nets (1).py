
# coding: utf-8

# In[70]:

import numpy as np
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.utils import np_utils
get_ipython().magic(u'matplotlib inline')


# In[136]:

mean1=[1.0,0.50]
mean2=[4.0,5.0]
con1=[[1.0,0],[0,3.0]]
con2=[[4.0,0],[0,2.0]]
pt1=np.random.multivariate_normal(mean1,con1,1000)
pt2=np.random.multivariate_normal(mean2,con2,1000)
plt.scatter(pt1[:,0],pt1[:,1],color='r')
plt.scatter(pt2[:,0],pt2[:,1],color='blue')
plt.show()


# In[138]:

X_data=np.concatenate((pt1,pt2),axis=0)
print X_data.shape
labels=np.concatenate((np.zeros(pt1.shape[0]),np.ones(pt2.shape[0])),axis=0)
print labels.shape
labels=labels.reshape(2000,1)
print labels.shape
labels=np.asarray(labels,dtype='int8')
labels=np_utils.to_categorical(labels,2)
print labels.shape
print labels


# In[139]:

model=Sequential()
model.add(Dense(5,input_dim=2))
model.add(Activation('relu'))
model.add(Dense(2))
model.add(Activation('tanh'))


# In[148]:

model.compile(optimizer='adagrad',loss='mean_squared_error')


# In[153]:

model.fit(X_data[:1500,:],labels[:1500,:],nb_epoch=10,batch_size=100,shuffle=True,validation_data=(X_data[1500:,:],labels[1500:,:]))

