#%%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = pd.read_csv( 'data\yahoo_SPDR S&P 500 ETF (SPY).csv', 
                    usecols=['Date','Close'], 
                    parse_dates=['Date'])
data.set_index('Date',inplace=True)
data = data.Close["2018":"2019"]

fig, ax = plt.subplots(figsize=(15,7))
data.plot(ax=ax)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))