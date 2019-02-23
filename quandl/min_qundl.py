#%%
import quandl
import pandas as pd
#%%
quandl.ApiConfig.api_key = "Your_API_Key"
df = pd.DataFrame(quandl.get("EIA/PET_RWTC_D"))
#%%
crisis = df["2007":"2009"]
crisis.plot()
