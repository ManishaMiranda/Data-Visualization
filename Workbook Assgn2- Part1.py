#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
import numpy as np 
import glob
all_data = pd.DataFrame() 
for f in glob.glob(r"C:\Users\maria\OneDrive\Documents\Data Visualization\datasets\weekly_call_data\weekdata*.xlsx"):  
    df = pd.read_excel(f)   
    all_data = all_data.append(df,ignore_index=True) 


# In[5]:


all_data.describe()


# In[ ]:




