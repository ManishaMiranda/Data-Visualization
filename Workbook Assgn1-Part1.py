#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,95,77,78,99] 
GradeList = zip(names,grades) 
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df.to_csv('studentgrades.csv',index=False,header=False)


# In[4]:


import pandas as pd 
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,95,77,78,99] 
bsdegrees = [1,1,0,0,1] 
msdegrees = [2,1,0,0,0] 
phddegrees = [0,1,0,0,0] 
Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees) 
columns = ['Names','Grades','BS','MS','PhD'] 
df = pd.DataFrame(data = Degrees, columns=columns) 
df
 


# In[12]:


import pandas as pd 
Location = r"C:\Users\maria\OneDrive\Documents\Data Visualization\datasets\gradedata.xlsx" 
df = pd.read_excel(Location)


# In[13]:


df.head()


# In[14]:


df.columns = ['first','last','sex','age','exer','hrs','grd','addr'] 
df.head()


# In[ ]:




