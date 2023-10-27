#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')

import datetime
import os


# In[5]:


tesla = pd.read_csv('Tesla_Stock.csv')
ford = pd.read_csv('Ford_Stock.csv')
gm = pd.read_csv('GM_Stock.csv')


# In[6]:


tesla.head()


# In[7]:


ford.head()


# In[12]:


gm.head()


# ### Stock 'Open Price' Plot :

# The "open price" in the context of financial markets refers to the price at which a particular security, such as a stock, commodity, or currency, starts trading at the beginning of a trading session or market opening. It is the first price at which a trade occurs after the market opens for the day or for a specific trading session.
# 
# The open price is a significant data point as it marks the starting point for that trading session, and it is often used in various financial analyses and charting, such as in the construction of candlestick charts. Traders and investors closely watch the open price, along with other price data, to assess market sentiment and make trading decisions.

# In[10]:


tesla['Open'].plot(label = 'Tesla', 
                   figsize = (12, 5), 
                   title = 'Open Price')
gm['Open'].plot(label = 'GM')
ford['Open'].plot(label = 'ford')
plt.legend()


# ### Volume Of Stock Traded:

# The volume of stock traded, or trading volume, is the total number of shares or the total value of shares bought and sold within a specific time frame, typically a day. It's a key indicator of market activity and liquidity, with high volume indicating strong interest and low volume suggesting the opposite. It can impact price movements, and traders use it to analyze market sentiment and make trading decisions.

# In[11]:


tesla['Volume'].plot(label = 'Tesla', 
                   figsize = (12, 5), 
                   title = 'Volume Traded')
gm['Volume'].plot(label = 'GM')
ford['Volume'].plot(label = 'ford')
plt.legend()


# Create a new column in each dataframe, and this new column will be called "Total Traded." To calculate what goes in this new column, multiply the "Open Price" by the "Volume Traded" for each row in the dataframe. This new "Total Traded" column will show the total value of shares traded for each entry, which is the amount of money exchanged at the opening price for that particular trade.

# In[13]:


tesla['Total Traded'] = tesla['Open']*tesla['Volume']
ford['Total Traded'] = ford['Open']*ford['Volume']
gm['Total Traded'] = gm['Open']*gm['Volume']


# In[16]:


tesla['Total Traded'].plot(label = 'Tesla', 
                           figsize = (12, 5))
ford['Total Traded'].plot(label = 'ford')
gm['Total Traded'].plot(label = 'gm')
plt.legend()
plt.ylabel('Total Traded')


# Plotting moving averages (MA) involves creating a graph that shows the average price of a stock over a certain number of days. It helps smooth out the ups and downs in stock prices, making it easier to see trends.
# 
# Here's how to plot the MA50 and MA200 for GM (General Motors):
# 
# 1. **MA50**: This is the average price of GM stock over the last 50 days. It helps you see short-term trends.
# 
# 2. **MA200**: This is the average price of GM stock over the last 200 days. It gives you a longer-term view of how the stock is doing.
# 
# When you plot these moving averages, you'll see two lines on a graph along with the actual GM stock price. These lines show you the average price over 50 and 200 days. By comparing them to the actual price, you can get a sense of whether the stock is on an upward or downward trend.
# 
# If the actual price is above both moving averages, it could be a sign of a strong uptrend. If it's below both moving averages, it might indicate a downtrend. These moving averages help investors make decisions about buying or selling GM stock based on trends in its price.

# In[18]:


gm['MA50'] = gm['Open'].rolling(50).mean()

gm['MA200'] = gm['Open'].rolling(200).mean()

gm[['Open','MA50','MA200']].plot(label = 'gm', 
                                 figsize = (12, 5))


# We want to check if car industry-related stocks, like GM and Ford, have a noticeable relationship. We'll create a scatter matrix plot by consolidating their opening prices into one dataset. This plot consists of pairs of scatter plots that show how the stocks' opening prices relate to each other. If we see a diagonal line going from the bottom left to the top right, it suggests a positive relationship (when one stock goes up, the other tends to go up), and the opposite for a line from the top left to the bottom right. This visual analysis will help us understand how these stocks are connected in terms of their opening prices.

# In[20]:


from pandas.plotting import scatter_matrix
car_company = pd.concat([tesla['Open'], gm['Open'], ford['Open']], axis = 1)
car_company.columns = ['Tesla Open','GM Open','Ford Open']
scatter_matrix(car_company, 
               figsize = (8,8),
               alpha = 0.2, 
               hist_kwds = {'bins':50});


# Creating a candlestick chart involves loading financial data into a DataFrame, using libraries like Matplotlib and mplfinance. You can customize the chart's style and appearance and then display it using plt.show(). This chart helps visualize the price movements of a financial instrument, like a stock, over time.

# $ r_t = \frac{p_t}{p_{t-1}} -1$

# This defines r_t (return at time t) as equal to the price at time t divided by the price at time t-1 (the previous day) minus 1. Basically this just informs you of your percent gain (or loss) if you bought the stock on day and then sold it the next day. While this isn't necessarily helpful for attempting to predict future values of the stock, its very helpful in analyzing the volatility of the stock. If daily returns have a wide distribution, the stock is more volatile from one day to the next. Let's calculate the percent returns and then plot them with a histogram, and decide which stock is the most stable!

# To add a new column called "returns" to each of your dataframes. This column will show how much the stock's price has changed from one day to the next. There are two common ways to calculate this change:
# 
# 1. **Using .shift()**: You can subtract the previous day's closing price from the current day's closing price. This tells you how much the price has moved from one day to the next.
# 
# 2. **Using pct_change method**: Alternatively, you can use a built-in function in pandas that does the same thing. It calculates the percentage change in price from one day to the next, which is essentially the same as the price change.
# 

# In[27]:


tesla['returns'] = (tesla['Close'] / tesla['Close'].shift(1) ) - 1


# In[28]:


tesla.head()


# In[32]:


tesla['returns'] = tesla['Close'].pct_change(1)
ford['returns'] = ford['Close'].pct_change(1)
gm['returns'] = gm['Close'].pct_change(1)


# In[30]:


tesla.head()


# In[33]:


ford.head()


# In[34]:


gm.head()


# In[36]:


gm['returns'].hist(bins=50)


# In[35]:


ford['returns'].hist(bins=50)


# In[37]:


tesla['returns'].hist(bins=50)


# In[40]:


tesla['returns'].hist(bins = 100, 
                      label = 'Tesla', 
                      figsize = (12, 5),
                      alpha = 0.5)
gm['returns'].hist(bins = 100,
                   label = 'GM', 
                   alpha = 0.5)
ford['returns'].hist(bins = 100,
                     label = 'Ford', 
                     alpha = 0.5)
plt.legend()


# In[41]:


tesla['returns'].plot(kind = 'kde',
                      label = 'Tesla',
                      figsize=(12,5))
gm['returns'].plot(kind = 'kde',
                   label = 'GM')
ford['returns'].plot(kind = 'kde',
                     label = 'Ford')
plt.legend()


# In[42]:


box_df = pd.concat([tesla['returns'], 
                    gm['returns'], 
                    ford['returns']],axis = 1)
box_df.columns = ['Tesla Returns',' GM Returns','Ford Returns']
box_df.plot(kind = 'box', 
            figsize = (8,11),
            colormap = 'jet')


# In[43]:


scatter_matrix(box_df, 
               figsize = (8,8),
               alpha = 0.2
               ,hist_kwds = {'bins':50});


# In[45]:


box_df.plot(kind = 'scatter',
            x = ' GM Returns', 
            y = 'Ford Returns',
            alpha = 0.4,
            figsize = (10,8))


# ## # Cumulative Daily Returns
# 
# To see which stock was the most wide ranging in daily returns (you should have realized it was Tesla, our original stock price plot should have also made that obvious).
# 
# With daily cumulative returns, the question we are trying to answer is the following, if I invested $1 in the company at the beginning of the time series, how much would is be worth today? This is different than just the stock price at the current day, because it will take into account the daily returns. Keep in mind, our simple calculation here won't take into account stocks that give back a dividend. Let's look at some simple examples:

# Lets us say there is a stock 'ABC' that is being actively traded on an exchange. ABC has the following prices corresponding to the dates given

#     Date                        Price
#     01/01/2018                   10
#     01/02/2018                   15
#     01/03/2018                   20
#     01/04/2018                   25

# **Daily Return** : Daily return is the profit/loss made by the stock compared to the previous day. (This is what ew just calculated above). A value above one indicates profit, similarly a value below one indicates loss. It is also expressed in percentage to convey the information better. (When expressed as percentage, if the value is above 0, the stock had give you profit else loss). So for the above example the daily returns would be
# 
# 
#     Date                         Daily Return                  %Daily Return
#     01/01/2018                 10/10 =  1                          -   
#     01/02/2018                 15/10 =  3/2                       50%
#     01/03/2018                 20/15 =  4/3                       33%
#     01/04/2018                 25/20 =  5/4                       20%

# **Cumulative Return**: While daily returns are useful, it doesn't give the investor a immediate insight into the gains he had made till date, especially if the stock is very volatile. Cumulative return is computed relative to the day investment is made.  If cumulative return is above one, you are making profits else you are in loss. So for the above example cumulative gains are as follows
# 
# 
#     Date                       Cumulative Return         %Cumulative Return
#     01/01/2018                  10/10 =  1                         100 %   
#     01/02/2018                  15/10 =  3/2                       150 %
#     01/03/2018                  20/10 =  2                         200 %
#     01/04/2018                  25/10 =  5/2                       250 %

# The formula for a cumulative daily return is:
# 
# $ i_i = (1+r_t) * i_{t-1} $
# 
# Here we can see we are just multiplying our previous investment at i at t-1 by 1+our percent returns. Pandas makes this very simple to calculate with its cumprod() method. Using something in the following manner:
# 
#     df[daily_cumulative_return] = ( 1 + df[pct_daily_return] ).cumprod()
#     

# In[52]:


tesla['Cumulative Return'] = (1 + tesla['returns']).cumprod()


# In[47]:


tesla.head()


# In[48]:


ford['Cumulative Return'] = (1 + ford['returns']).cumprod()
gm['Cumulative Return'] = (1 + gm['returns']).cumprod()


# To determine which stock showed the highest and lowest return for a 1 dollor investment, first calculate the cumulative returns for each stock and then plot them against the time series index. The stock with the highest cumulative return will be the one that turned a 1 dollor investment into the most money, while the stock with the lowest cumulative return will be the least profitable.

# In[50]:


tesla['Cumulative Return'].plot(label = 'Tesla',
                                figsize = (12, 5), 
                                title = 'Cumulative Return')
ford['Cumulative Return'].plot(label = 'Ford')
gm['Cumulative Return'].plot(label = 'GM')
plt.legend()


# In[ ]:




