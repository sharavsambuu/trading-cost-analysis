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
df_ = pd.read_csv("./data/USDJPY.csv", parse_dates=True, index_col="datetime")


#%%


#%%
timeframe_by_hours  = 24
timeframe_by_minute = timeframe_by_hours*60


#%%
timeframe_by_minute = 30


#%%
timeframe = f"{timeframe_by_minute}Min"

df = df_.resample(timeframe).agg({'Open':'first', 'High':'max', 'Low':'min', 'Close':'last', 'Volume': 'sum'})
df.dropna(inplace=True) # Dropping because of FX doesn't trade during weekends

df


#%%


#%%


#%%
rsi_period = 14
sigma      = 2.0

df[f"rsi_{rsi_period}"] = talib.RSI(df['Close'], timeperiod=rsi_period)

rsi_values = df[f"rsi_{rsi_period}"].values
rsi_values = rsi_values[~np.isnan(rsi_values)]

rsi_mean, rsi_stdev = norm.fit(rsi_values)
print(f"mean    : {rsi_mean}")
print(f"std.dev : {rsi_stdev}")

sigma_lower = round(rsi_mean - sigma*rsi_stdev, 1)
sigma_upper = round(rsi_mean + sigma*rsi_stdev, 1)

print(f"sigma lower : {sigma_lower}")
print(f"sigma upper : {sigma_upper}")

_, axs = plt.subplots(1, figsize=(12, 8))
axs.hist(df[f"rsi_{rsi_period}"].values, bins=150, range=(0.0, 100.0));
plt.axvline(x=sigma_lower, color='b', label = 'sigma lower', linestyle='--')
plt.axvline(x=sigma_upper, color='b', label = 'sigma upper', linestyle='--')


#%%


#%%
# RSI signals extraction 

rsi_upper  = sigma_upper
rsi_lower  = sigma_lower


df['position'] = np.nan
# Long positions, if RSI cross up rsi_lower level
df.loc[
    (df[f"rsi_{rsi_period}"].shift(1)<rsi_lower) & (df[f"rsi_{rsi_period}"]>=rsi_lower),
    'position'] = 1
# Short position, if RSI cross down rsi_upper level
df.loc[
    (df[f"rsi_{rsi_period}"].shift(1)>rsi_upper) & (df[f"rsi_{rsi_period}"]<=rsi_upper),
    'position'] = -1

df['position'].value_counts()


#%%


#%%
plot_df = df["2020-01-12 10:00:00":"2022-03-10"].copy(deep=True)

plot_df['rsi_lower'     ] = rsi_lower
plot_df['rsi_upper'     ] = rsi_upper
plot_df['short_position'] = np.nan
plot_df['long_position' ] = np.nan
plot_df['short_position'] = plot_df[plot_df['position']==-1]['Close']
plot_df['long_position' ] = plot_df[plot_df['position']== 1]['Close']

apds = [
    mpf.make_addplot(plot_df['long_position' ], panel=0, type='scatter', markersize=120, marker='^', color='g'),
    mpf.make_addplot(plot_df['short_position'], panel=0, type='scatter', markersize=120, marker='v', color='r'),
    mpf.make_addplot(plot_df[f"rsi_{rsi_period}"], panel=1),
    mpf.make_addplot(plot_df[f"rsi_lower"], panel=1, color='g', linestyle='--'),
    mpf.make_addplot(plot_df[f"rsi_upper"], panel=1, color='r', linestyle='--'),
    ]

mpf.plot(
    plot_df, type='candle', addplot=apds, figsize=(22, 10), figscale=1.6, 
    title=f"RSI{rsi_period}, timeframe {timeframe_by_minute}",
    style='binance', volume=True, volume_panel=2, panel_ratios=(6,2,1), show_nontrading=False
    )


#%%


#%%


#%%
# Mapping entry prices from higher timeframe to lower timeframe in order to analyze slippages
# Scenario is like when signal is generated based on Close price of higher timerframe, so we 
# are kind of hopefully open a position on that Close price will be executed fairly, but
# in reality there will be a lot of fluctuations in the lower timeframe so there is no guarentee,
# meaning order will be executed at different price which is called Slippage. 
# So taking into account slippage into trading strategy development would prevent losses occured
# by this phenomenom and of course strategy will be more realistic tho.

df_eval = df_.copy()

df_eval['long_entry' ] = np.nan
df_eval['short_entry'] = np.nan

for idx, row in df[df['position']==1].iterrows():
    if idx in df_eval.index:
        df_eval.at[idx, 'long_entry'] = float(row['Close'])

for idx, row in df[df['position']==-1].iterrows():
    if idx in df_eval.index:
        df_eval.at[idx, 'short_entry'] = float(row['Close'])

look_ahead_shift = 1
df_eval['long_entry' ] = df_eval['long_entry' ].shift(timeframe_by_minute+look_ahead_shift)
df_eval['short_entry'] = df_eval['short_entry'].shift(timeframe_by_minute+look_ahead_shift)

# Multiple scenarios are like how many minutes after an order executed.
for executed_after_minute in range(1, 4+1):
    df_eval[f"Close_{executed_after_minute}"            ] = df_eval[f"Close"].shift(-executed_after_minute)
    df_eval[f"long_slippage{executed_after_minute}_pct" ] = np.nan
    df_eval[f"short_slippage{executed_after_minute}_pct"] = np.nan

# How much changes by percentage occured after order executed
for executed_after_minute in range(1, 4+1):
    df_eval[f"long_slippage{executed_after_minute}_pct" ] = (df_eval[f"Close_{executed_after_minute}"] - df_eval[f"long_entry" ])/df_eval['long_entry' ]
    df_eval[f"short_slippage{executed_after_minute}_pct"] = (df_eval[f"Close_{executed_after_minute}"] - df_eval[f"short_entry"])/df_eval['short_entry']

# Convert slippage by percentage to slippage by bps
for executed_after_minute in range(1, 4+1):
    df_eval[f"long_slippage{executed_after_minute}_bps" ] = (df_eval[f"long_slippage{executed_after_minute}_pct" ]*100.0)
    df_eval[f"short_slippage{executed_after_minute}_bps"] = (df_eval[f"short_slippage{executed_after_minute}_pct"]*100.0)



#%%


#%%


#%%
# Slippage by bps distribution after order executed x minutes

_, axs = plt.subplots(2, 2, figsize=(18, 8))

range_by_bps = (-1.0, 1.0)

l11 = axs[0,0].hist(df_eval[df_eval[f"long_slippage1_bps" ].notnull()][f"long_slippage1_bps" ].values, bins=300, range=range_by_bps, label="Long slippage BPS" , color='g')
l12 = axs[0,0].hist(df_eval[df_eval[f"short_slippage1_bps"].notnull()][f"short_slippage1_bps"].values, bins=300, range=range_by_bps, label="Short slippage BPS", color='r')
axs[0,0].set_title(f"RSI{rsi_period}, timeframe {timeframe_by_minute}m, slippage after 1m by BPS")

l21 = axs[0,1].hist(df_eval[df_eval[f"long_slippage2_bps" ].notnull()][f"long_slippage2_bps" ].values, bins=300, range=range_by_bps, label="Long slippage BPS" , color='g')
l22 = axs[0,1].hist(df_eval[df_eval[f"short_slippage2_bps"].notnull()][f"short_slippage2_bps"].values, bins=300, range=range_by_bps, label="Short slippage BPS", color='r')
axs[0,1].set_title(f"RSI{rsi_period}, timeframe {timeframe_by_minute}m, slippage after 2m by BPS")

l31 = axs[1,0].hist(df_eval[df_eval[f"long_slippage3_bps" ].notnull()][f"long_slippage3_bps" ].values, bins=300, range=range_by_bps, label="Long slippage BPS" , color='g')
l32 = axs[1,0].hist(df_eval[df_eval[f"short_slippage3_bps"].notnull()][f"short_slippage3_bps"].values, bins=300, range=range_by_bps, label="Short slippage BPS", color='r')
axs[1,0].set_title(f"RSI{rsi_period}, timeframe {timeframe_by_minute}m, slippage after 3m by BPS")

l41 = axs[1,1].hist(df_eval[df_eval[f"long_slippage4_bps" ].notnull()][f"long_slippage4_bps" ].values, bins=300, range=range_by_bps, label="Long slippage BPS" , color='g')
l42 = axs[1,1].hist(df_eval[df_eval[f"short_slippage4_bps"].notnull()][f"short_slippage4_bps"].values, bins=300, range=range_by_bps, label="Short slippage BPS", color='r')
axs[1,1].set_title(f"RSI{rsi_period}, timeframe {timeframe_by_minute}m, slippage after 4m by BPS")

plt.tight_layout()
plt.show();


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%

