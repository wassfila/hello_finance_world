#%%
import json
import quandl
import matplotlib.pyplot as plt
import pandas as pd
config = json.load(open("api_key.json"))
#%%
quandl.ApiConfig.api_key = config['quandl']
data = quandl.get("EIA/PET_RWTC_D")
df = pd.DataFrame(  data)
#%%
print(df.dtypes)
print("--- shape ---")
print(df.shape)
print("--- head ---")
print(df.head())
#%%
plt.plot(df)
#%%
few_years = df["2011":"2019"]
few_years.plot()
