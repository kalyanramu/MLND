
# coding: utf-8

# In[88]:

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
import os

# In[90]:

def ExtractVals(lines):
    vals=[]
    for i,line in enumerate(lines):
        number = re.findall("\d+\.\d+", line)
        if number !=[]:
            vals.append(number[0])
    return vals      


# In[110]:

def plot_state_exploration(filename,num_states=4):
    fname = os.path.join("logs", filename)
    #print(fname)
    with open(fname) as f:
        content = f.readlines()
    data = content[4:]
    Qvals = ExtractVals(data)
    Qvalues = np.reshape(Qvals, (num_states, len(Qvals)/num_states)).T 

    states_cnt =[]
    for row in Qvalues:
        cnt = 0
        for val in row:
            if float(val) !=0.00:
                cnt +=1
        states_cnt.append(cnt)  
    plt.hist(states_cnt,len(states_cnt))
    plt.xticks(range(num_states+1))
    plt.xlabel('Total Count of Actions Explored')
    plt.ylabel('Number of States')
    plt.grid(True)
    plt.show()




