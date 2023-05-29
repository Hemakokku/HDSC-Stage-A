#!/usr/bin/env python
# coding: utf-8

# # HDSC-Introduction-to-Python-for-machine-learning

# In[1]:


import pandas as pd 
df = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv',encoding='cp1252')
df


# In[2]:


df.describe()


# In[3]:


df.isnull()


# In[4]:


df.corr()


# In[5]:


# Accessing specific columns/features
area_code = df['Area Code']
area = df['Area']
item_code = df['Item Code']
item = df['Item']
element_code = df['Element Code']
element = df['Element']
unit = df['Unit']
y2014 = df['Y2014']
y2015 = df['Y2015']
y2016 = df['Y2016']
y2017 = df['Y2017']
y2018 = df['Y2018']


# In[6]:


# Perform basic operations on the dataset
# Example: Calculate the total production for each year
total_production = df[['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']].sum()


# In[8]:


# Display the total production for each year
print(total_production)


# In[9]:


# Example: Filter the dataset based on a condition
filtered_data = df[df['Area'] == 'Your Desired Area']


# In[10]:


# Display the filtered data
print(filtered_data)


# In[11]:


df.shape


# In[12]:


len(df)


# In[13]:


df.iloc[:]


# In[14]:


df.loc()


# In[15]:


df.groupby('Item')['Y2015'].sum()


# In[16]:


df.groupby('Area')['Y2017'].sum()


# In[17]:


df.groupby('Element').sum()


# In[ ]:




