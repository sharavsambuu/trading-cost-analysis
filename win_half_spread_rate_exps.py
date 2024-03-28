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
broker_shift = dt.timedelta(minutes=0)


#%%
def load_prev_ticks(mt5, instrument):
    if not mt5.initialize():
        mt5.shutdown()
    datetime_now   = dt.datetime.now(utc_tz) - broker_shift
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
    return df[['bid', 'ask', 'volume']]



#%%
def load_latest_ticks(mt5, instrument, delta_seconds=40):
    if not mt5.initialize():
        mt5.shutdown()
    utc_now   = dt.datetime.now(utc_tz) - broker_shift
    utc_from  = utc_now - dt.timedelta(seconds=delta_seconds)
    new_ticks = mt5.copy_ticks_range(instrument, utc_from, utc_now, mt5.COPY_TICKS_ALL)
    df             = pd.DataFrame(new_ticks)
    df['datetime'] = pd.to_datetime(df['time_msc'], unit='ms').dt.tz_localize(utc_tz)
    df = df.set_index(pd.DatetimeIndex(df['datetime']))
    df['volume'  ] = 1
    mt5.shutdown()
    return df[['bid', 'ask', 'volume']]


#%%
def aggregate_bars(input_ticks, timeframe='1min'):
    ticks                     = input_ticks.copy()
    ticks['spread'          ] = ticks['ask'] - ticks['bid']
    ticks['half_spread'     ] = ticks['spread'] / 2.0
    ticks['mid_price'       ] = (ticks['ask'] + ticks['bid']) / 2.0
    ticks['half_spread_rate'] = ticks['half_spread']/ticks['mid_price']
    x_df = ticks.resample(timeframe).agg({
            'mid_price'        : 'ohlc',
            'volume'           : 'sum' , # Volume
            'spread'           : 'mean', # Spread
            'half_spread_rate' : 'mean'  # Half Spread Rate
        })
    x_df.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Spread', 'HalfSpreadRate']
    return x_df.iloc[:-1]


#%%
instrument = "EURUSD"
all_ticks  =  load_prev_ticks(mt5=mt5, instrument=instrument)

m_df  = aggregate_bars(all_ticks, '1min')
m_len = len(m_df)

print(f"loaded 1minute bars, len : {m_len}")
print(m_df)

#sys.exit()

while True:
    new_ticks = load_latest_ticks(mt5=mt5, instrument=instrument, delta_seconds=80)
    all_ticks = pd.concat([all_ticks, new_ticks])
    all_ticks = all_ticks[~all_ticks.index.duplicated(keep='last')]
    all_ticks = all_ticks.dropna()

    m_df      = aggregate_bars(all_ticks, '1min')
    new_m_len = len(m_df)

    if new_m_len>m_len:
        m_len = new_m_len
        print('\n\n')
        print(f"new bar is created, len={m_len}")
        print('--------')
        print(m_df)


    time.sleep(3)
    pass


#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%



#%%


