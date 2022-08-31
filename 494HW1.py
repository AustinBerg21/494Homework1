#!/usr/bin/env python
# coding: utf-8

# In[11]:



import numpy as np
import scipy as sp


# In[12]:


from scipy.optimize import minimize
from scipy.optimize import LinearConstraint
from scipy.optimize import Bounds
from numpy import array


# In[32]:


# Function
def f(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    x5 = x[4]
    return (x1-x2)**2+(x2+x3-2)**2+(x4-1)**2+(x5-1)**2
# Initial Guess
x0 = [0,1,1,1,1]
# List Constraints
cons = ({'type':'eq','fun': lambda x: x[0] + 3*x[1]},
         {'type':'eq','fun': lambda x: x[2] + x[3] - 2*x[4]},
         {'type':'eq','fun': lambda x: x[1] - x[4]})
# List Bounds
bounds = Bounds([-10,-10,-10,-10,-10], [10,10,10,10,10])


# In[31]:


res=minimize(f,x0, bounds = bounds, constraints = cons)


# # print(res)

# In[15]:





# In[ ]:





# In[ ]:




