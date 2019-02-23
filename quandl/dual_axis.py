#%%
import json
import quandl
import pandas as pd
config = json.load(open("api_key.json"))
quandl.ApiConfig.api_key = config['quandl']

df_eia = pd.DataFrame(quandl.get("EIA/PET_RWTC_D"))
df_oil = pd.DataFrame(quandl.get("NSE/OIL.1"))
df_eia_recent = df_eia["2016":"2019"]
df_oil_recent = df_oil["2016":"2019"]
#%%
fig,ax = plt.subplots()
ax3= ax.twinx()
ax3.spines['right'].set_position(('axes', 1.0))
ax3.set_ylabel('eia_g')
ax.set_ylabel('oil_c')
df_eia_recent.plot(ax=ax,style='g-', figsize=(20,10))
df_oil_recent.plot(ax=ax3,style='c-' , figsize=(20,10))
