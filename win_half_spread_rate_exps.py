#%%
import os 
import sys
import pytz
import requests
import time
import datetime    as dt
import pandas      as pd
import numpy       as np
import MetaTrader5 as mt5


#%%


#%%
utc_tz       = pytz.timezone("Etc/UTC")
broker_shift = dt.timedelta(hours=0)


#%%
def load_prev_ticks(mt5, instrument):
    print("loading previous ticks...")
    if not mt5.initialize():
        mt5.shutdown()
    datetime_now   = dt.datetime.now(utc_tz) + broker_shift
    yesterday      = datetime_now - dt.timedelta(days=15)
    start_datetime = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
    end_datetime   = datetime_now
    previous_ticks = mt5.copy_ticks_range(
        instrument        , 
        start_datetime    , 
        end_datetime      , 
        mt5.COPY_TICKS_ALL
        )
    df             = pd.DataFrame(previous_ticks)
    df['datetime'] = pd.to_datetime(df['time_msc'], unit='ms').dt.tz_localize(utc_tz)
    df = df.set_index(pd.DatetimeIndex(df['datetime']))
    df['volume'  ] = 1
    mt5.shutdown()
    print("previous ticks are loaded now.")
    return df[['bid', 'ask', 'volume']]
    return df

df = load_prev_ticks(mt5=mt5, instrument="USDJPY")
print(df)



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%


