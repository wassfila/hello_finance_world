#%%
import matplotlib.pyplot as plt
import pandas as pd
#%%
df_sp = pd.read_csv("data\yahoo_SPDR S&P 500 ETF (SPY).csv",
                    index_col="Date", 
                    squeeze=True )
df_world = pd.read_csv("data\yahoo_iShares Core MSCI World UCITS ETF.csv",
                    index_col="Date", 
                    squeeze=True )
#%%
print(df_sp.dtypes)
print(df_world.dtypes)
print("--- shape ---")
print(df_sp.shape)
print(df_world.shape)
print("--- head ---")
print(df_sp.head())
print(df_world.head())
#%%
df_world.plot(figsize=(20,10), y=["Close"])
#%%
df_world_recent = df_world.Close["2018":"2019"]
df_world_recent.plot(figsize=(20,10))
#%%
def plot_two(A,B,label_A="",label_B=""):
    fig,ax = plt.subplots()
    ax3= ax.twinx()
    ax3.spines['right'].set_position(('axes', 1.0))
    ax.set_ylabel(label_A)
    ax3.set_ylabel(label_B)
    A.plot(ax=ax,style='c-', figsize=(20,10),label=label_A)
    B.plot(ax=ax3,style='g-' , figsize=(20,10),label=label_B)
    ax.legend(loc='upper left')
    ax3.legend(loc='upper right')
    return

sp_recent = df_sp.Close["2018":"2019"]
world_recent = df_world.Close["2018":"2019"]
plot_two(sp_recent,world_recent,"SP","World")
