#%%
import warnings
warnings.filterwarnings("ignore")
def action_with_warnings():
    warnings.warn("should not appear")
with warnings.catch_warnings(record=True):
    action_with_warnings()
import norgatedata
import quantstats        as qs
import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt




#%%


#%%
def download_history(symbol, start_date):
    return norgatedata.price_timeseries(
        symbol,
        stock_price_adjustment_setting = norgatedata.StockPriceAdjustmentType.TOTALRETURN,
        padding_setting                = norgatedata.PaddingType.NONE,
        start_date                     = start_date,
        timeseriesformat               = 'pandas-dataframe',
        )

#%%


#%%
df = download_history("SPY", "2000-01-01")
df

#%%


#%%
df['Close'].plot()


#%%
short_window = 50
long_window  = 252

short_ma = df['Close'].rolling(window=short_window, min_periods=short_window).mean()
long_ma  = df['Close'].rolling(window=long_window , min_periods=long_window ).mean()

signals = pd.DataFrame(index=df.index)
signals['signal'  ] = 0.0  # Set the default to be 0
signals['short_ma'] = short_ma
signals['long_ma' ] = long_ma

signals['signal'][signals['short_ma'] > signals['long_ma']] = 1
signals['signal'][signals['short_ma'] < signals['long_ma']] = -1


tgt_vol = 0.15

returns_df = df['Close'].pct_change()

signals['stdev'] = returns_df.rolling(22).std() * np.sqrt(252)  # Convert to annualized standard deviation

# Calculate volatility target weights
signals['vol_tgt'] = tgt_vol / signals['stdev']

# Clip weights to a maximum of 1 to avoid leverage
# Here we use 2x leverage to make sure we can hit our volatility target of 15%
signals['vol_tgt'] = signals['vol_tgt'].clip(0, 2)

# Adjust the signal by the volatility target, lagging both to avoid look-ahead bias
vol_signal = signals['signal'].shift(1) * signals['vol_tgt'].shift(1)

# Compute returns for the volatility-targeted strategy
strategy_voltgt_returns = returns_df * vol_signal

((strategy_voltgt_returns + 1).cumprod()-1).plot(title='Cum Returns')
plt.ylabel('Total Returns')
plt.show()

#%%


#%%
turnover = abs(vol_signal.diff())

# Shift by -1 to get the date at which the transaction occurred, which was at close yesterday.
turnover = turnover.shift(-1)
turnover.plot(title='Turnover', figsize=(14, 5))
plt.show()


#%%


#%%
# Compute brokerage fees
brokerage_fees = 0.0020  # 20 basis points
brokerage = turnover * brokerage_fees

# Plot Brokerage
brokerage.plot(title='Brokerage', figsize=(14, 5))
plt.show()


#%%
# Plot Cum Brokerage
(brokerage.cumsum()*100).plot(title='Brokerage', figsize=(14, 5))
plt.ylabel('Brokerage Fees in %')
plt.show()


#%%
# Compute Spread fee
bid_ask_fee =0.000032  # 0.32 basis points
spread = turnover * bid_ask_fee

# Plot Brokerage
spread.plot(title='Spread', figsize=(14, 5))
plt.show()

#%%
# Plot Cum Spread
(spread.cumsum()*100).plot(title='Spread', figsize=(14, 5))
plt.ylabel('Fees in %')
plt.show()


#%%


#%%
# Volume on SPY is massive, we are probably never going to be 1% of ADV
daily_value = df['Volume'] * df['Close']
daily_value.plot(title='Value Traded', figsize=(14, 5))
plt.ylabel('USD Traded')
plt.show()

#%%
# Lets assume we are going to have a maximum of 1'000'000 USD traded on any day, therefor
adv = 1000000 / daily_value
adv.plot(title='Average Daily Value', figsize=(14, 5))
plt.show()

#%%
# Lets use this to compute slippage costs, linearly (This is not the Linear Model)
# If 1% = 10 basis points then every 10 basis points of ADV can be 1 basis point of slippage.
cost = (adv / 0.01) * 0.0010
slippage = cost * turnover

# Plot total slippage
slippage.cumsum().plot(title='Total Slippage', figsize=(14, 5))
plt.ylabel('Slippage')
plt.show()

#%%
# Total Slippage is less 25 basis points for the entire period, assuming a max $1Million a day transaction


#%%
total_costs = slippage + spread + brokerage

# Plot total costs
total_costs.cumsum().plot(title='Total Costs: Slippage + Spread + Brokerage', figsize=(14, 5))
plt.ylabel('Fees')
plt.show()

#%%


#%%
# Plot the cumulative rets (compounded growth)
# Before costs
((strategy_voltgt_returns + 1).cumprod()-1).plot()

# After Costs
after_cost = strategy_voltgt_returns - total_costs 
((after_cost + 1).cumprod()-1).plot(figsize = (12, 8))

# Plot Cum returns
plt.title('Cumulative Returns')
plt.legend(['Before Costs', 'After Costs'])
plt.ylabel('Total Returns')
plt.show()


#%%
sr_before = strategy_voltgt_returns.mean() / strategy_voltgt_returns.std() * np.sqrt(252)
sr_after  = after_cost.mean() / after_cost.std() * np.sqrt(252)

print(f'Sharpe Ratio Before: {sr_before.round(2)}')
print(f'Sharpe Ratio After: {sr_after.round(2)}')

#%%


#%%


#%%


#%%



#%%


