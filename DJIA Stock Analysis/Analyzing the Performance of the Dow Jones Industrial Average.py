#!/usr/bin/env python
# coding: utf-8

# ## Analyzing the Performance of the Dow Jones Industrial Average

# The main goal of this project is to analyze the historical performance of the DJIA and make informed predictions or conclusions about its future trends.

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn')

import yfinance as yf
import warnings
warnings.filterwarnings('ignore')


# In[2]:


url = 'https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average'

dataframe = pd.read_html(url)[1]

dataframe


# In[3]:


dataframe.rename(columns = {'Date added':'Date_Added'}, inplace = True)
dataframe.rename(columns = {'Index weighting': 'Weights'}, inplace = True)


# In[4]:


dataframe


# In[5]:


dataframe.Date_Added = pd.to_datetime(dataframe.Date_Added)


# In[6]:


dataframe.Weights= pd.to_numeric(dataframe.Weights.str.replace('%', ''))


# In[7]:


dataframe


# In[8]:


dataframe.info()


# In[9]:


dataframe.columns


# In[10]:


dataframe.drop(columns = 'Notes', inplace = True)


# In[11]:


dataframe.head()


# In[12]:


dataframe.set_index('Symbol', inplace = True)


# In[13]:


dataframe


# In[14]:


symbols = dataframe.index.to_list()
symbols


# In[18]:


last_update = dataframe['Date_Added'].max()
last_update


# In[19]:


time_series = yf.download(tickers = symbols, start = last_update)
time_series


# In[21]:


time_series.Close


# In[22]:


time_series.dropna(inplace = True)


# In[23]:


performance = time_series.Close.iloc[-1].div(time_series.Close.iloc[0]).sub(1).sort_values(ascending = False)
performance


# In[24]:


performance.index.name = 'Symbol'


# In[25]:


performance


# In[26]:


dataframe


# In[27]:


dataframe['performance'] = performance


# In[28]:


dataframe


# In[29]:


dataframe.sort_values(by = 'performance', ascending = False)


# This project will provide you with a comprehensive understanding of the DJIA's historical performance, help you develop data analysis and modeling skills, and potentially offer insights for making informed investment decisions.
# 
# 
# 
# 
# 
# 

# In[ ]:




