#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy 


# In[4]:


arr = numpy.array([1,2,3,4,5])
a


# In[5]:


# Array generte 
name = numpy.array(["kKhan","bhai","Sindh","punjabi","pakistani"])
print(name)


# In[6]:


import numpy as np 


# In[39]:


uni = np.array(["IBA","muet","quest","lums"])


print(uni)


# In[10]:


print(np.__version__)


# In[13]:


num =np.array((1,2,4,5,7))
print(num)


# In[18]:


#create the 2D arrays 
import numpy as np
num1 = np.array([[1, 2, 3], [6,7,3] ])
print(num1)


# In[41]:


arr = np.array([[1, 2, 3], [4, 5, 6]])
b = np.where(arr == 5)

print(b)


# In[21]:


#3D array gerente 
arr =np.array([[[1,2,],[3,4]], [[6,7],[5,6]]])
print(arr)


# In[23]:


print(arr.ndim)
print(num1.ndim)
print(uni.ndim)
print(name.ndim)


# In[33]:


arr = np.array([[1, 2, 3], [4, 5, 6]])
arr = np.where(arr==2)
print(arr)


# In[43]:


arr = np.array([1,2,4,5,4,6,3,5,])
x = np.where(arr == 4)
print(x)
print(np.sort(arr))


# In[58]:


# random numbers access in arrray with help of numpy libarary
from numpy import random

x=random.randint(50,size=(2,5))


print(x)


# In[ ]:





# In[ ]:





# In[ ]:




