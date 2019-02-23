#dates API
# https://matplotlib.org/api/dates_api.html
#%%
import json
import urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as dates
#%%
config = json.load(open("api_key.json"))

def alpha_url(symbol,interval):
    base_query = "https://www.alphavantage.co/query"
    function = "?function=TIME_SERIES_INTRADAY"
    api_key = "&apikey="+config['alphavantage']
    symbol_query = "&symbol="+symbol
    interval_query = "&interval="+interval
    datatype = "&datatype=csv"
    url = base_query + function + api_key + symbol_query + interval_query + datatype
    return url

#%%
microsoft = pd.read_csv(alpha_url("MSFT","30min"),
                    parse_dates=['timestamp'])
microsoft.set_index('timestamp',inplace=True)

#%%
print(microsoft.dtypes)
print("--- shape ---")
print(microsoft.shape)
print("--- head ---")
print(microsoft.head())
#%%
fig, ax = plt.subplots(figsize=(20,10))
microsoft.plot(ax=ax,y=["close"],figsize=(20,10))
ax.xaxis.set_major_locator(dates.HourLocator())

#%%
microsoft = pd.read_csv(alpha_url("MSFT","30min"),
                    parse_dates=['timestamp'])
microsoft.set_index('timestamp',inplace=True)
fig, ax = plt.subplots(figsize=(20,10))
microsoft.plot(ax=ax,y=["close"],figsize=(20,10))
ax.xaxis.set_major_locator(dates.DayLocator())
