import json
import urllib.request
import pandas as pd
import dash_app as app


config = json.load(open("../api_key.json"))

def alpha_url(symbol,interval):
    base_query = "https://www.alphavantage.co/query"
    function = "?function=TIME_SERIES_INTRADAY"
    api_key = "&apikey="+config['alphavantage']
    symbol_query = "&symbol="+symbol
    interval_query = "&interval="+interval
    datatype = "&datatype=csv"
    url = base_query + function + api_key + symbol_query + interval_query + datatype
    return url

url = alpha_url("MSFT", "30min")
print(url)
microsoft = pd.read_csv(url)

app.set_data(microsoft,"Microsoft")
app.run()
