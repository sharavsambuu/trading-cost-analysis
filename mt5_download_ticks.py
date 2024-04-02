import os
import sys
import time
import pytz
from pytz import timezone
import datetime
import calendar
import dateutil.relativedelta
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5

# 
# Usage:
#
#   Last 5 months of tick data download
#
#   python mt5_download_ticks.py usdjpy 5
#
#

instrument   = sys.argv[1]
month_counts = int(sys.argv[2])

if instrument:
    if not os.path.exists('data_mt5_ticks/'+instrument):
        os.makedirs('data_mt5_ticks/'+instrument)

utc_tz       = pytz.timezone("Etc/UTC")
broker_shift = datetime.timedelta(minutes=0)


datetime_now = datetime.datetime.now(utc_tz)

for m in reversed(range(1, month_counts+1)):
    prev_datetime    = datetime_now + dateutil.relativedelta.relativedelta(months=-m)
    _, days_of_month = calendar.monthrange(prev_datetime.year, prev_datetime.month)
    start_datetime = prev_datetime.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    end_datetime   = prev_datetime.replace(day=days_of_month, hour=23, minute=59, second=59, microsecond=0)

    if not mt5.initialize():
        mt5.shutdown()
    
    new_ticks = mt5.copy_ticks_range(instrument.upper(), start_datetime, end_datetime, mt5.COPY_TICKS_ALL)
    
    df             = pd.DataFrame(new_ticks)
    df['datetime'] = pd.to_datetime(df['time_msc'], unit='ms').dt.tz_localize(utc_tz)
    df = df.set_index(pd.DatetimeIndex(df['datetime']))
    
    filename = f"{instrument}_{prev_datetime.year}_{prev_datetime.month}_ticks.csv"
    df[['bid', 'ask']].to_csv('./data_mt5_ticks/'+instrument+"/"+filename, header=True)
    print(filename, "is saved.")

    mt5.shutdown()