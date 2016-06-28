
# coding: utf-8

# In[27]:

from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[37]:

digit=load_digits()
print(digits.data.shape)
plt.imshow(digits.images[8]) 
plt.show()
plt.imshow(digits.images[7])
plt.show()
print digits.images[8]
print digits.images[7]


# In[ ]:



