#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("select block which should not be in edit mode then press a for add row above press b for add row below, and press x for delete")


# In[1]:


print('hello world')


# In[2]:


print('shift + enter for run prgramm')


# ### Array operation 

# In[ ]:


print('for header add ### for size and save it and select that block and press m')


# In[ ]:


print('pyhon int has not limit ram is a limit for size of int')


# In[5]:


import numpy as np


# In[7]:


num = np.array([32,43,234,53,34,33,64,98])


# In[6]:


print(num)


# In[8]:


print(num)


# In[9]:


num


# In[10]:


num.dtype


# In[11]:


num.size


# In[12]:


num[3]


# In[13]:


num[3]=100
num[3]


# In[14]:


num[3]=43.43


# In[16]:


num=np.array([ 32,  43, 24.90,  43,  34,  33,  64,  98])


# In[17]:


num=np.array([ 32,  43, 24.90,  43,  34,  33,  64,  98])


# In[18]:


num


# In[19]:


num=np.array([ 32,  43, 24.90,  43,  'hello',  33,  64,  98])


# In[20]:


num


# In[21]:


print('if we change one elements data type then it will change all arrays datatype')


# In[22]:


print('java and pythone use unocode and c and cpp use ascii')


# In[23]:


print("हेलो वर्ल्ड")


# In[24]:


num1 = np.array([पुणे , मुंबई ])
num1


# In[25]:


num1 = np.array(["पुणे" , "मुंबई" ])
num1


# In[26]:


print('uicode support all languages but ascii only support english language')


# In[27]:


num1[0]*5


# num.max()

# In[28]:


num.max()


# In[29]:


num=np.array([ 32,  43, 24.90,  43,  34,  33,  64,  98])
num.max()


# In[30]:


num.sort()


# In[31]:


help(num)


# In[32]:


num*2


# In[33]:


x=[ 32,  43, 24.90,  43,  34,  33,  64,  98]
x*2


# In[36]:


a=np.array([ 32,  43, 24.90,  43,  34,  33,  64,  98])
            
            


# In[37]:


a*2


# In[38]:


num>50


# In[39]:


a>50


# In[40]:


a


# In[41]:


a*2>50


# In[42]:


100 in a


# In[43]:


100 not in a


# In[44]:


list(range(10))


# In[45]:


list(range(1,11))


# In[46]:


np.arange(1,11)


# In[48]:


m=tuple(range(5,100,5))


# In[49]:


m


# In[50]:


np.arange(1,10,0.5)


# In[51]:


np.zeros(10)
np.ones(11)
np.empty(10) #garbage values


# In[52]:


np.ones(11)


# In[53]:


np.empty(10) #garbage values


# In[56]:


np.linspace(1,10,20)


# In[57]:


9.05263158 -8.57894737


# In[58]:


6.68421053 -6.21052632


# In[59]:


np.linspace(1,10,2)


# In[60]:


# 1 element in array called scalar
# 1d array called vector
# 2d array called matrix


# In[61]:


x = np.array([[4,3,2],[43,3,2]])
x


# In[62]:


x[1][1]


# In[63]:


x.shape


# In[64]:


x.size


# In[66]:


q= np.array([[23,32,32],[3,32,9]])
q


# In[67]:


x.reshape(6,1)


# In[68]:


x.reshape(3,2)


# In[70]:


x.reshape(2,3)


# In[71]:


x.reshape(-1,1)


# In[72]:


#convert 2d array in 1d
x.flatten()


# In[73]:


x


# #panda has two data strture i.e. series(1d) and deta frames(2d)

# Panda

# In[75]:


import pandas as pd


# In[76]:


s = pd.Series([32,89,32,43,23])
s


# In[77]:


s[1]=55
s


# In[80]:


#series contain homogenous data, only replace is possible , can't change size , and indexing is user define 
s=pd.Series([43,43,43,6,43,1,64],index=range(100,107))
s


# #data frame is collection of series of same length, it is 2d

# In[82]:


x = pd.Series([1,2,3,4,5])
y = pd.Series(['fds','hhl','jlkj','fds','rew'])
z = pd.Series([12.2,43.9,90.3,32.9,54.0])


# In[83]:


df = pd.DataFrame({
    'roll':x,
    'name':y,
    'marks':z
})
df


# In[87]:


m= df.roll=1


# In[88]:


m


# In[93]:


print(df.get(1))


# In[94]:


df.columns


# In[95]:


df.T


# In[96]:


df.roll[1]=2


# In[98]:


df.roll[2]=3
df.roll[3]=4
df.roll[4]=5


# In[99]:


df


# In[100]:


df.values


# In[101]:


df


# In[113]:


print(df.loc[[1]])


# In[108]:


print(df.loc[1,'name'])


# In[111]:


print(df.iloc[1,:3])


# In[ ]:




