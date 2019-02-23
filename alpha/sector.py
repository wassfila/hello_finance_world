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

def alpha_sector_url():
    base_query = "https://www.alphavantage.co/query?function=SECTOR&apikey=demo"
    function = "?function=SECTOR"
    api_key = "&apikey="+config['alphavantage']
    url = base_query + function + api_key
    return url

#%%
response = urllib.request.urlopen(alpha_sector_url())
data = response.read().decode('utf-8')
print(data)
