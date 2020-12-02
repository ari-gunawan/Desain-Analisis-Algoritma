#!/usr/bin/env python
# coding: utf-8

# ## Directed graphs

# In[4]:


import networkx as nx
import matplotlib.pyplot as plt 

G = nx.MultiDiGraph()

G.add_edges_from([
    (1, 2),
    (2, 3),
    (3, 2),
    (2, 1),
    (1, 4),
    (4, 1),
    (3, 4),
    (4, 3)di
    
])

plt.figure(figsize=(8,8))
nx.draw(G)


# In[ ]:




