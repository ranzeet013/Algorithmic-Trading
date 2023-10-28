#!/usr/bin/env python
# coding: utf-8

# ## Data Scraping :

# Data scraping, or web scraping, is the process of automatically collecting information from websites or online sources. It's used for various purposes like research, competitor analysis, and more. The process involves accessing a website, extracting specific data from it, and storing that data for analysis. It should be done ethically and within legal boundaries, and you should be aware of the website's terms of service and any anti-scraping measures in place. There are programming libraries and tools available to make web scraping easier. Always consider legal and ethical implications when scraping data from the web.

# In[1]:


import pandas as pd
import numpy as np
import yfinance as yf


# The code extracts the list of S&P 500 company symbols from a Wikipedia page, downloads historical stock data for these companies from Yahoo Finance spanning eight years up to '2023-9-27', and structures the data into a DataFrame. It then applies the `describe()` function to provide summary statistics for the numerical columns in the DataFrame, offering insights into the historical performance of these S&P 500 companies.

# In[3]:


sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]

sp500['Symbol'] = sp500['Symbol'].str.replace('.', '-')

symbol_list = sp500['Symbol'].unique().tolist()

end_date = '2023-9-27'

start_date = pd.to_datetime(end_date) - pd.DateOffset(365 * 8)

dataframe = yf.download(tickers = symbol_list, 
                        start = start_date, 
                        end = end_date).stack()

dataframe.index_names = ['date', 'tickers']

dataframe.columns = dataframe.columns.str.lower()

dataframe 


# In[4]:


dataframe.to_csv('sp500.csv')


# In[ ]:




