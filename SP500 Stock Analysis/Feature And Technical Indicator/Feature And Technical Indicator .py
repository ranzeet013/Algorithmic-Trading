#!/usr/bin/env python
# coding: utf-8

# ### Calculating features and technical indicator for each stocks :

# When analyzing stocks, it's crucial to consider various features and technical indicators that provide insights into their price movements and trading dynamics.

# 
# - **Garman-Klass Volatility**: Measures historical price volatility.
# - **RSI (Relative Strength Index)**: Identifies overbought or oversold conditions.
# - **Bollinger Bands**: Gauges price volatility and potential reversals.
# - **ATR (Average True Range)**: Assesses market volatility.
# - **MACD (Moving Average Convergence Divergence)**: Identifies trend changes.
# - **Dollar Volume**: Evaluates stock liquidity for trading decisions.

# ###  Garman-Klass Volatility:

# Garman-Klass is a method to calculate historical volatility. It's used to measure the degree of variation in a stock's price over time. A higher Garman-Klass value implies higher price volatility.
# 
# 1. **Measure of Price Volatility:** Garman-Klass Volatility is a way to measure how much a stock's price goes up and down over time.
# 
# 2. **Helps Assess Risk:** It's a tool to understand the risk associated with a stock. Higher Garman-Klass values indicate higher risk.
# 
# 3. **Useful for Traders and Investors:** Traders and investors use it to make informed decisions, especially when they want to know how much a stock's price might change in the future.
# 
# 4. **Historical Data:** It looks at past price movements to estimate future volatility.
# 
# 5. **Part of Risk Management:** It's an important part of risk management in the world of finance, helping people make decisions about buying or selling stocks.

# \begin{equation}
# \text{Garman-Klass Volatility} = \frac{(\ln(\text{High}) - \ln(\text{Low}))^2}{2} - (2\ln(2) - 1)(\ln(\text{Adj Close}) - \ln(\text{Open}))^2
# \end{equation}

# In[6]:


dataframe['german_class_vol'] = ((np.log(dataframe['high']) - np.log(dataframe['low'])) ** 2) / 2 - (2 * np.log(2) -1 )*((np.log(dataframe['adj close']) - np.log(dataframe['open']))** 2)


# In[7]:


dataframe.head()


# ### RSI (Relative Strength Index):

# RSI is a momentum oscillator that measures the speed and change of price movements. It ranges from 0 to 100 and is typically used to identify overbought or oversold conditions. An RSI above 70 may indicate overbought, while below 30 may indicate oversold.

# 1. **Momentum Indicator:** RSI is a popular momentum indicator used in trading.
# 
# 2. **Measures Overbought and Oversold Conditions:** It quantifies the speed and change of price movements and provides a value between 0 and 100. Values above 70 typically suggest an asset is overbought, while values below 30 indicate oversold conditions.
# 
# 3. **Identifies Potential Reversals:** Traders use RSI to identify potential reversal points in the market. 
# 
# 4. **Helps in Timing Trades:** RSI is valuable for timing entry and exit points in trading strategies. 
# 
# 5. **Simple to Use:** It's easy to understand and implement, making it a popular tool for both novice and experienced traders.

# In[8]:


dataframe['rsi'] = dataframe.groupby(level = 1)['adj close'].transform(lambda x: pandas_ta.rsi(close = x, length = 20))


# In[9]:


dataframe.head(10)


# ### Bollinger Bands :

# Bollinger Bands consist of a middle band (usually a simple moving average), an upper band, and a lower band. They are used to measure price volatility. The upper and lower bands are placed a certain number of standard deviations away from the middle band.

# 1. **Volatility Indicator:** Bollinger Bands are a volatility indicator used in technical analysis.
# 
# 2. **Consist of Three Lines:** They consist of three lines on a price chart: a middle band (usually a simple moving average), an upper band, and a lower band.
# 
# 3. **Measures Price Volatility:** The bands expand and contract based on price volatility. When they widen, it indicates higher volatility, and when they contract, it indicates lower volatility.
# 
# 4. **Identifies Potential Reversals:** Bollinger Bands help traders identify potential price reversals and overbought or oversold conditions.
# 
# 5. **Useful for Range-Bound Markets:** They are particularly useful in range-bound markets, helping traders spot potential breakout points.
# 
# 6. **Widely Used:** Bollinger Bands are widely used by traders to make trading decisions and set stop-loss orders.

# In[10]:


dataframe['bb_low'] = dataframe.groupby(level = 1)['adj close'].transform(lambda x: pandas_ta.bbands(close = np.log1p(x), length = 20).iloc[:, 0])


# In[11]:


dataframe['bb_mid'] = dataframe.groupby(level = 1)['adj close'].transform(lambda x: pandas_ta.bbands(close = np.log1p(x), length = 20).iloc[:, 1])


# In[13]:


dataframe['bb_high'] = dataframe.groupby(level = 1)['adj close'].transform(lambda x: pandas_ta.bbands(close = np.log1p(x), length = 20).iloc[:, 2])


# In[14]:


dataframe.head()


# ### ATR (Average True Range):

# 
# 
# ATR measures market volatility by calculating the average range between the daily high and low prices. It helps traders identify the level of price movement and can be useful for setting stop-loss orders.

# 
# 1. **Volatility Measurement:** ATR, or Average True Range, is a popular technical indicator that measures the volatility or price movement of an asset.
# 
# 2. **Daily Range Consideration:** It calculates the average range between the daily high and low prices, taking into account any potential price gaps from the previous day.
# 
# 3. **Helps Set Stop Losses:** Traders use ATR to determine appropriate stop-loss levels. A higher ATR suggests the need for a wider stop loss, reflecting greater price volatility.
# 
# 4. **Useful for Risk Management:** ATR is an essential tool for managing risk in trading, helping traders make decisions about position sizing and risk tolerance.
# 
# 5. **Numeric Value:** ATR is expressed as a numeric value, which indicates the average price range for a specific period. Higher values imply greater volatility.

# In[16]:


def compute_atr(stock_data):
    atr = pandas_ta.atr(high = stock_data['high'], 
                        low = stock_data['low'], 
                        close = stock_data['close'], 
                        length = 14)
    return atr.sub(atr.mean()).div(atr.std())

dataframe['atr'] = dataframe.groupby(level = 1, group_keys = False).apply(compute_atr)


# In[17]:


dataframe


# ### MACD (Moving Average Convergence Divergence):

# 
# 
# MACD is a trend-following momentum indicator that shows the relationship between two moving averages of a security's price. It includes a MACD line, a signal line, and a histogram. MACD crossovers and divergences are used to spot potential buy and sell signals.

# 1. **Trend-Following Indicator:** MACD is a popular trend-following momentum indicator used in technical analysis.
# 
# 2. **Consists of Three Components:** MACD includes the MACD line (the fast line), the signal line (a smoothed version of the MACD line), and a histogram that represents the difference between these two lines.
# 
# 3. **Identifies Trend Changes:** It helps traders identify potential changes in the direction of a trend. Bullish signals occur when the MACD crosses above the signal line, and bearish signals occur when it crosses below.
# 
# 4. **Measures Momentum:** MACD quantifies the momentum of price movements, indicating whether a stock is gaining or losing momentum.
# 
# 5. **Useful for Trading Signals:** Traders often use MACD crossovers and divergences to generate buy and sell signals for various assets.
# 
# 6. **Widely Adopted:** MACD is widely adopted in the trading community and is considered a versatile and valuable tool for assessing price trends and potential trade opportunities.

# In[19]:


def compute_macd(close):
    macd = pandas_ta.macd(close = close, length = 20).iloc[:, 0]
    return macd.sub(macd.mean()).div(macd.std())

dataframe['macd'] = dataframe.groupby(level = 1, group_keys = False)['adj close'].apply(compute_macd)


# In[20]:


dataframe


# ### Dollar Volume:

# 
# 
# Dollar volume is a measure of a stock's liquidity, calculated by multiplying the stock's trading volume by its price. It helps traders assess how actively a stock is traded and is essential for assessing the ease of buying or selling a particular stock.

# 1. **Liquidity Measure:** Dollar Volume is a metric used to gauge the liquidity of a stock or asset.
# 
# 2. **Calculates Total Value:** It calculates the total value of the shares traded for a particular stock by multiplying the trading volume (number of shares traded) by the stock's price.
# 
# 3. **Assesses Trading Activity:** Dollar Volume helps assess how actively a stock is traded in terms of actual dollars, making it essential for evaluating ease of buying or selling.
# 
# 4. **Determines Market Interest:** Higher Dollar Volume indicates a greater level of market interest in a stock, while lower Dollar Volume suggests less interest.
# 
# 5. **Used for Trade Decisions:** Traders often consider Dollar Volume when making trading decisions, especially when dealing with more liquid stocks.
# 
# 6. **Valuable for Risk Management:** It's a valuable tool for risk management, as stocks with higher Dollar Volume are generally easier to enter and exit positions without significantly impacting prices.

# In[21]:


dataframe['dollor_vol'] = (dataframe['adj close'] * dataframe['volume']) / 1e6


# In[22]:


dataframe 


# In[23]:


dataframe.to_csv('technical_feature_ind.csv')


# In[ ]:




