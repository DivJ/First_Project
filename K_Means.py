
# coding: utf-8

# In[176]:

import numpy as np
import math
from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[291]:

mean1=[1,4]
mean2=[10,4]
cov1=[[5,1],[0,1]]
cov2=[[10,10],[0,1]]
dist1=np.random.multivariate_normal(mean1,cov1,50)
dist2=np.random.multivariate_normal(mean2,cov2,50)
plt.scatter(dist1[:,0],dist1[:,1] )
plt.scatter(dist2[:,0],dist2[:,1])
pt=np.concatenate((dist1,dist2),axis=0)


# In[305]:

dist=[]
lab=[]
x_sum,y_sum=0,0
x_sum1,y_sum1=0,0
k=2
mean=pt[:k]

def assignment():
    global dist
    global lab
    for i in range(0,100):
        for j in range(0,k):
            dist.append(math.hypot(pt[i,0]-mean[j,0],pt[i,1]-mean[j,1]))
        lab.append(dist.index(min(dist)))
        dist=[]

def mean_shift():
    global x_sum,x_sum1,y_sum,y_sum1,lab
    for i in range(0,100):
        if(lab[i]==0):
            plt.scatter(pt[i,0],pt[i,1],c='r')
            x_sum=pt[i,0]+x_sum
            y_sum=pt[i,1]+y_sum
        
        elif(lab[i]==1):
            plt.scatter(pt[i,0],pt[i,1],c='b')
            x_sum1=pt[i,0]+x_sum1
            y_sum1=pt[i,1]+y_sum1
        
        
    
    mean[0,0]=x_sum/lab.count(0)
    mean[0,1]=y_sum/lab.count(0)
    mean[1,0]=x_sum1/lab.count(1)
    mean[1,1]=y_sum1/lab.count(1)
    
    lab=[]
    
    
    
    
def k_means(itr):
    for z in range(0,itr):
        assignment()
        mean_shift()
k_means(100)
        






    

