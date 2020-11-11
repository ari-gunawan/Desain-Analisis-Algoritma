#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


myWeb = nx.DiGraph()
myPages = range(1,5)


# In[6]:


connections = [(1,2),(1,4),(1,5),(1,6),(2,1),(2,3),(3,2),(3,4),(4,1),(4,3),(5,1),(5,6),(6,1),(6,5)]
myWeb.add_nodes_from(myPages)
myWeb.add_edges_from(connections)


# In[7]:


pos=nx.shell_layout(myWeb)
nx.draw(myWeb, pos, arrows=True, with_labels=True)
plt.show()


# In[10]:


def createPageRank(aGraph):
    nodes_set = len(aGraph)
    M = nx.to_numpy_matrix(aGraph)
    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))
    prob_outwards = np.array(
        [1.0/count
        if count>0 else 0.0 for count in outwards])
    G = np.asarray(np.multiply(M.T, prob_outwards))
    p = np.ones(nodes_set)/float(nodes_set)
    if np.min(np.sum(G, axis=0)) < 1.0:
        print('WARN: G is substochactis')
    return G,p


# In[11]:


G,p = createPageRank(myWeb)
print(G)


# In[ ]:




