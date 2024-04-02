#%%
import sys
import os

import pandas as pd


#%%
df = pd.read_csv("./data_mt5_ticks/usdjpy_2024_ticks.csv", index_col='datetime', parse_dates=True)
df = df.dropna()

df

#%%


#%%
df['spread'] = df['ask'] - df['bid']
df

#%%
df['spread'].hist(bins=300)


#%%
df[df['spread']>0.15]


#%%


#%%
df['half_spread'     ] = df['spread'] / 2.0
df['mid_price'       ] = (df['ask'] + df['bid']) / 2.0
df['half_spread_rate'] = df['half_spread'] / df['mid_price']*100.0

#%%


#%%
df

#%%


#%%
df['half_spread_rate'].hist(bins=300)


#%%


#%%
df['spread'].mean(), df['spread'].median(), df['spread'].min(), df['spread'].max()


#%%
df['half_spread_rate'].mean(), df['half_spread_rate'].median(), df['half_spread_rate'].min(), df['half_spread_rate'].max()

#%%


#%%


#%%


#%%


#%%


#%%


#%%


# %%

