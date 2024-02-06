#%%
# MA Cross Backtesting on 1H BTC with following trade costs and timeframes
# - Slippage and commission  is 0.0015 as specified by AlgoVibes
# - Initial capital is 10000.0$
# - Timeframe is 1H
# 

#%%
import warnings
warnings.filterwarnings("ignore")
def action_with_warnings():
    warnings.warn("should not appear")
with warnings.catch_warnings(record=True):
    action_with_warnings()
import yfinance          as yf
import pandas            as pd
import numpy             as np
import quantstats        as qs
import matplotlib.pyplot as plt

#%%


#%%
df = yf.download('BTC-USD', interval='1h', period='23mo')
df

#%%
df['Close'].plot()

#%%
df['Price'] = df['Open'].shift(-1)

df

#%%


#%%
# Signal extraction

df['MA50' ] = df['Close'].rolling(window=20).mean()
df['MA200'] = df['Close'].rolling(window=50).mean()

df['Signal'] = 0
df.loc[((df['MA50'] > df['MA200']) & (df['MA50'].shift(1) <= df['MA200'].shift(1))), 'Signal'] =  1
df.loc[((df['MA50'] < df['MA200']) & (df['MA50'].shift(1) >= df['MA200'].shift(1))), 'Signal'] = -1

#%%
df['Signal'].value_counts()

#%%


#%%
plot_df = df["2023-02-01":"2023-03-10"]

fig, ax1 = plt.subplots(1, figsize=(28, 12), sharex=True)

ax1.plot(plot_df.index, plot_df['Close'], label='Close', color='black')
ax1.plot(plot_df['MA200'], color='blue' )
ax1.plot(plot_df['MA50' ], color='green')
ax1.plot(plot_df[plot_df['Signal'] ==  1].index, plot_df[plot_df['Signal'] ==  1]['Price'], '^', markersize=8, color='green', label='Long' )
ax1.plot(plot_df[plot_df['Signal'] == -1].index, plot_df[plot_df['Signal'] == -1]['Price'], 'v', markersize=8, color='red'  , label='Short')
ax1.set_ylabel('Price')
ax1.set_title('BTC-USD Signals')
ax1.legend()
ax1.grid()

plt.tight_layout()
plt.show()

#%%


#%%
# Position tracking with slippage

slippage_commission = 0.0015
position            = 0
in_position         = False
entry_timestamp     = None
entry_price         = 0
exit_timestamp      = None
exit_price          = 0
position_history    = []

for index, row in df.iterrows():
    if row['Signal'] != 0:
        in_position = False
    
    if not in_position:
        exit_timestamp = index
        exit_price     = row['Price']
        pct_change     = position * (exit_price - entry_price) / entry_price - slippage_commission
        position_history.append((entry_timestamp, exit_timestamp, entry_price, exit_price, pct_change))
        pass

    # Enter new position
    if row['Signal'] == 1 and not in_position:
        entry_timestamp = index
        entry_price     = row['Price']
        position        = 1
        in_position     = True
    if row['Signal'] == -1 and not in_position:
        entry_timestamp = index
        entry_price     = row['Price']
        position        = -1
        in_position     = True
       
        


#%%
position_df = pd.DataFrame(position_history, columns=['Entry Time', 'Exit Time', 'Entry Price', 'Exit Price', 'Pct Change'])
position_df['cumret' ] = position_df['Pct Change'].cumsum()
position_df['cumprod'] = (position_df['Pct Change']+1).prod()


#%%


#%%
position_df['cumret'].plot()

#%%


#%%


#%%
initial_capital    = 10000.0 # Initial capital in dollars
commission_fee     = 0.05    # 0.05% commission fee per trade
position_per_trade = 0.02    # 2% of position size per trade

account_balance = initial_capital
balance_changes = []

# Iterate through each trade in the position history
for index, trade in position_df.iterrows():
    pct_change       = trade['Pct Change']
    position_size    = account_balance * position_per_trade
    dollar_change    = position_size * pct_change
    commission       = position_size * (commission_fee/100.0)
    balance_change   = dollar_change - commission
    account_balance += balance_change
    balance_changes.append(balance_change)

position_df['Balance Change'] = balance_changes
position_df['Account History'] = initial_capital + position_df['Balance Change'].cumsum()

position_df['Entry Time'] = pd.to_datetime(position_df['Entry Time'])
position_df = position_df.set_index('Entry Time')

position_df['Account Change'] = position_df['Account History'].pct_change()


#%%
position_df

#%%


#%%
qs.plots.snapshot(position_df['Account Change'], title='MA Cross on BTC YFinance Performance', show=True);

#%%
qs.plots.drawdown(position_df['Account Change'])

#%%
qs.plots.drawdowns_periods(position_df['Account Change'])

#%%
qs.plots.histogram(position_df['Account Change'])

#%%
qs.plots.monthly_heatmap(position_df['Account Change'])

#%%
qs.stats.sharpe(position_df['Account Change'])

#%%
position_df["Account History"].plot()

#%%


#%%


#%%


#%%
