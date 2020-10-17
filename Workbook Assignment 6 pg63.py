#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


def score_to_numeric(x):
    if x=='female':
        return 1
    if x=='male':
        return 0


# In[3]:


df.head()


# In[4]:


df['gender_val'] = df['gender'].apply(score_to_numeric)
df.tail()


# In[21]:


import statsmodels.formula.api as sm
result = sm.ols(
         formula ='grade ~ age + exercise + hours',
         data = df).fit()
result.summary()


# In[22]:


import statsmodels.formula.api as sm
result = sm.ols(
         formula ='grade ~ age + exercise + hours + gender_val',
         data = df).fit()
result.summary()


# In[23]:


import statsmodels.formula.api as sm
result = sm.ols(
         formula ='grade ~ exercise + hours + gender_val',
         data = df).fit()
result.summary()


# In[24]:


import statsmodels.formula.api as sm
result = sm.ols(
         formula ='grade ~ exercise + hours',
         data = df).fit()
result.summary()


# In[ ]:




