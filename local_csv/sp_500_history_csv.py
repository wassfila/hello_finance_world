#%%
import matplotlib.pyplot as plt
import pandas as pd
#%%
df = pd.read_csv("data\yahoo_SPDR S&P 500 ETF (SPY).csv", 
                    index_col="Date", 
                    squeeze=True )
print(df.dtypes)
print("--- shape ---")
print(df.shape)
print("--- head ---")
print(df.head())
#%%
df.plot(figsize=(20,10), y=["High","Low"])
