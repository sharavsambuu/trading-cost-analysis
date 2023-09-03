#%%
import warnings
warnings.filterwarnings("ignore")
def action_with_warnings():
    warnings.warn("should not appear")
with warnings.catch_warnings(record=True):
    action_with_warnings()
import os
import sys
import csv
import talib
from   scipy.stats       import norm
import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt
import mplfinance        as mpf


#%%


#%%


#%%
usdjpy_df_ = pd.read_csv("./data/avatrade_mt5/klines/1m/USDJPY.csv", parse_dates=True, index_col="datetime")
eurusd_df_ = pd.read_csv("./data/avatrade_mt5/klines/1m/EURUSD.csv", parse_dates=True, index_col="datetime")

#%%


#%%
usdjpy_df_["2020-01-01":]['Spread'].hist(bins=250, range=(0, 50))


#%%
eurusd_df_["2020-01-01":]['Spread'].hist(bins=250, range=(0, 60))


#%%


#%%
# rolling averages of spreads
window = 4*60 # 4 hours rolling
usdjpy_df_['average_spread'] = usdjpy_df_['Spread'].rolling(window=window).mean()
eurusd_df_['average_spread'] = eurusd_df_['Spread'].rolling(window=window).mean()


#%%
timeframe_by_hours  = 4
timeframe_by_minute = timeframe_by_hours*60


#%%


#%%
timeframe = f"{timeframe_by_minute}Min"

usdjpy_df = usdjpy_df_.resample(timeframe).agg({'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Volume': 'sum', 'average_spread':'last'})
eurusd_df = eurusd_df_.resample(timeframe).agg({'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Volume': 'sum', 'average_spread':'last'})

usdjpy_df.rename(columns={"average_spread": "Spread"}, inplace=True)
eurusd_df.rename(columns={"average_spread": "Spread"}, inplace=True)

usdjpy_df.dropna(inplace=True) # Dropping because of FX doesn't trade during weekends
eurusd_df.dropna(inplace=True) # Dropping because of FX doesn't trade during weekends



#%%


#%%
usdjpy_df

#%%
eurusd_df

#%%


#%%
usdjpy_df["2020-01-01":]['Spread'].hist(bins=250, range=(0, 30))


#%%
eurusd_df["2020-01-01":]['Spread'].hist(bins=250, range=(0, 15))


#%%


#%%


#%%
usdjpy_df["2020-01-01":]['Spread'].mean()


#%%
eurusd_df["2020-01-01":]['Spread'].mean()


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%

