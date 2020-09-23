#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


print(np.__version__)


# In[9]:


def getFirst(myList):
    return myList[0]


# In[10]:


getFirst([1,2,3])


# In[11]:


def getSum(myList):
    sum = 0
    for item in myList:
        sum = sum+item
    return sum
#perharikan posisi spasi pada return


# In[13]:


getSum([1,2,3,4])


# In[17]:


def getSum(myList):
    sum = 0
    for row in myList:
        for item in row:
            sum += item
    return sum


# In[18]:


getSum([[1,2,5],[3,4,7]])


# In[24]:


def searchBinary(myList,item):
    first = 0
    last = len(myList)-1
    foundFlag = False
    while( first<=last and not foundFlag):
        mid = (first + last)//2
        if myList[mid] == item :
            foundFlag = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag


# In[28]:


searchBinary([8,9,10,100,1000,2000,3000], 10)


# In[29]:


searchBinary([8,9,10,100,1000,2000,3000], 5)

