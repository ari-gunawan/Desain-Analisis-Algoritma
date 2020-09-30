#!/usr/bin/env python
# coding: utf-8

# # 1.1 List

# In[ ]:


aList = ["John", 33,"Toronto",True]


# In[4]:


aList


# In[5]:


type(aList)


# In[6]:


bin_colors=['Red','Green','Blue','Yellow']


# # Tuples 

# In[14]:


bin_colors=('Red','Green','Blue','Yellow')
print(f"The second element of the tuples is {bin_colors[1]}")


# In[17]:


print(f"The elements after thrid element onwards are {bin_colors[2:]}")


# In[21]:


nested_tuple = (1,2,(100,200,300),6)
print(f"The maximum value of the inner tuple {max(nested_tuple[2])}")


# # 1.2 Dictionary

# In[26]:


bin_colors ={
    "manual_color": "Yellow",
    "approved_color": "Green",
    "refused_color": "Red",
}


# In[27]:


print(bin_color)


# In[28]:


bin_colors.get('approved_color')


# In[29]:


bin_colors['approved_color']


# In[30]:


bin_colors['approved_color']="Purple"


# In[31]:


print(bin_colors)


# # 1.3 Sets

# In[1]:


green = {'grass', 'leaves'}
print(green)


# In[2]:


yellow = {'dendelions','fire hydrant', 'leaves'}
red = {'fire hydrant', 'blood', 'rose', 'leaves'}


# In[3]:


print(f"The union of yellow and red sets is {yellow|red}")


# In[4]:


print(f"The intersaction of yellow and red s {yellow&red}")


# # 5. Data Frames

# ## 1.4 DataFrame

# In[8]:


import pandas as pd
df = pd.DataFrame([
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Steven', 40, True]])
df.columns = ['id','name','age','decision']
print(df)


# ## 1.4.1 Column Selection

# In[9]:


df[['name','age']]


# The positioning of column is deterministic in a data frame. Fourth column can be retrieved by its position as follow:

# In[10]:


df.iloc[:,3]


# ## 1.4.2 Row Selection

# In[11]:


df.iloc[1:3,:]


# In[12]:


df[df.age>30]


# ## 1.5 Matrix

# In[13]:


import numpy as np
myMatrix = np.array([[11,22,13],[21,22,23],[31,32,33]])


# In[15]:


print(myMatrix)


# In[16]:


print(type(myMatrix))


# In[17]:


myMatrix.transpose()


# # Vector

# In[18]:


myVector = [22,33,44,55]


# In[19]:


print(type(myVector))


# In[22]:


myVector = np.array([22,33,44,55])
print(myVector)


# In[23]:


print(type(myVector))


# # Stack

# In[32]:


class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


# # Populate the stack

# In[34]:


stack=Stack()
stack.push('Red')
stack.push('Green')
stack.push("Blue")
stack.push("Yellow")


# ## Pop

# In[35]:


stack.pop()


# In[36]:


stack.isEmpty()


# In[37]:


colors = ['Red']


# In[38]:


colors.append('Green')
colors.append('Yellow')
colors.append('Blue')


# In[39]:


colors


# # Queue

# In[49]:


class Queue(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items ==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)


# In[50]:


queue = Queue()


# In[51]:


queue.enqueue("Red")


# In[52]:


queue.enqueue('Green')


# In[53]:


queue.enqueue('Blue')


# In[54]:


queue.enqueue('Yellow')


# In[55]:


print(f"Size of queue is {queue.size()}")


# In[56]:


print(queue.dequeue())


# In[ ]:




