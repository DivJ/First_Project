
# coding: utf-8

# In[81]:

from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
import numpy as np
from keras.utils import np_utils
from keras.layers import Dense,Activation
from keras.models import Sequential
get_ipython().magic(u'matplotlib inline')


# In[155]:

digits=load_digits()                    #loading images from datasets
print digits.data.shape
plt.imshow(digits.images[1791],cmap='gray')
plt.show()


# In[162]:

x_data=[]
for i in range(1797):
    x_data.append(digits.images[i].flatten())
x_data=np.asarray(x_data)            #loading images array to x_data set
print x_data.shape


# In[163]:

labels=digits.target
labels=np.asarray(labels).reshape(1797,1)
print labels.shape
labels=np_utils.to_categorical(labels,10)
print labels.shape


# In[164]:

model=Sequential()
model.add(Dense(5,input_dim=64))
model.add(Activation('sigmoid'))
model.add(Dense(10))
model.add(Activation('tanh'))


# In[165]:

model.compile(optimizer='adadelta',loss='binary_crossentropy')


# In[166]:

model.fit(x_data[:1500,:],labels[:1500,:],nb_epoch=20,batch_size=50,shuffle=True,validation_data=(x_data[1500:,:],labels[1500:,:]))


# In[167]:

scores=model.evaluate(x_data,labels)
print scores


# In[169]:

y_train_pred = model.predict_classes(x_data, verbose=0)
print('First 3 predictions: ', y_train_pred[:3])


# In[ ]:



