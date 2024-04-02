#%%
import sys
import os

import pandas as pd


#%%


#%%
csv_files = [f"{fname}" for fname in os.listdir("./data_mt5_ticks") if fname.endswith(".csv")]
csv_files


#%%
index_list                   = []
half_spread_rate_mean_list   = []
half_spread_rate_median_list = []
half_spread_rate_min_list    = []
half_spread_rate_max_list    = []

for fname in csv_files:
    instrument = fname.replace("_2024_ticks.csv", "")
    df = pd.read_csv(f"./data_mt5_ticks/{instrument}_2024_ticks.csv", index_col='datetime', parse_dates=True)
    df = df.dropna()

    df['spread'          ] = df['ask'] - df['bid']
    df['half_spread'     ] = df['spread'] / 2.0
    df['mid_price'       ] = (df['ask'] + df['bid']) / 2.0
    df['half_spread_rate' ] = df['half_spread'] / df['mid_price'] * 100

    index_list                  .append(instrument)
    half_spread_rate_mean_list  .append(df['half_spread_rate'].mean())
    half_spread_rate_median_list.append(df['half_spread_rate'].median())
    half_spread_rate_min_list   .append(df['half_spread_rate'].min())
    half_spread_rate_max_list   .append(df['half_spread_rate'].max())

stats_df = pd.DataFrame(index=index_list)
stats_df['half_spread_rate_mean'  ] = half_spread_rate_mean_list
stats_df['half_spread_rate_median'] = half_spread_rate_median_list
stats_df['half_spread_rate_min'   ] = half_spread_rate_min_list
stats_df['half_spread_rate_max'   ] = half_spread_rate_max_list

stats_df

#%%


#%%


#%%


#%%


#%%


#%%


#%%


# %%

