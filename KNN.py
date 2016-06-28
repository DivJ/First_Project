
# coding: utf-8

# In[4]:

import matplotlib.pyplot as plt
import numpy as np
import random
import math
get_ipython().magic(u'matplotlib inline')


# In[5]:

mean1=[1,4]
mean2=[3,4]
cov1=[[5,0],[0,1]]
cov2=[[2,0],[0,2]]
dist1=np.random.multivariate_normal(mean1,cov1,100)
dist2=np.random.multivariate_normal(mean2,cov2,100)
plt.scatter(dist1[:,0],dist1[:,1] )
plt.scatter(dist2[:,0],dist2[:,1],c='r' )
plt.show()


# In[6]:

pt1=np.concatenate((dist1,dist2),axis=0)
pt2=np.concatenate((np.zeros(dist1.shape[0]),np.ones(dist2.shape[0])),axis=0)


# In[7]:

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(pt1,pt2)


# In[8]:

print(neigh.predict([0,1]))
print(neigh.predict([6,6]))


# In[17]:

def Knn(X_train,Y_train,X_test,k):
    dist=[]
    i=0;
    while i<200:
        dist.append(math.hypot(X_train[i,0]-X_test[0],X_train[i,1]-X_test[1]))
        i+=1
    dist=np.asarray(dist)
    list1=np.concatenate((dist,Y_train.T),axis=1)
    final=sorted(list1, key=list1[0])
    final=np.asarray(final)
    while i<200:
        if final[i,1]==0:
            count0=count0+1
        elif final[i,1]==1:
            count1=count1+1
        i+=1
    if count0>count1:
        print "Point Belongs To Set A"
    if count0<count1:
        print "Point Belongs To Set B"
X_test=np.array([1,2])
Knn(pt1,pt2,X_test,3)
    


# In[16]:

print most_common(1,2,3,4,5,1,2,1,2)

