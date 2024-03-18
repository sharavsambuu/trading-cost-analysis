#%%
import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt
from   datetime          import timedelta

#%%


#%%


#%%
# Preparing data for portfolio

num_securities = 30
num_periods    = 200
start_date     = pd.to_datetime('2022-01-01')
end_date       = pd.to_datetime('2023-12-31')

trade_dates    = pd.to_datetime(np.sort(np.random.choice(pd.date_range(start=start_date, end=end_date, periods=num_periods + 1), num_periods, replace=False)))

df = pd.DataFrame({'datetime'  : trade_dates})
df['datetime' ] = pd.to_datetime(df['datetime'])
df['datetime_'] = df['datetime']
df = df.set_index('datetime')

outliers_percentage = 20.0
outliers_percentage = outliers_percentage/100.0 # percentage of all returns are outliers
outliers_count      = int(num_periods*outliers_percentage)

for idx in range(0, num_securities):
    percentage_changes = np.random.uniform(-0.045, 0.055, num_periods).astype(float)
    extreme_returns    = np.random.uniform(-0.09,  0.1, outliers_count).astype(float)
    outliers_date      = df['datetime_'].sample(n=outliers_count).to_list()
    df[f"return_{idx}"] = percentage_changes
    for outlier in list(zip(outliers_date, extreme_returns)):
        outlier_dt  = outlier[0]
        outlier_ret = outlier[1]
        df.loc[outlier_dt, f"return_{idx}"] = outlier_ret
    df[f"cum_ret_{idx}"  ] = df[f"return_{idx}"].cumsum()

df.drop('datetime_', axis=1, inplace=True)

df


#%%
#for idx in range(0, num_securities):
#    df[f'cum_ret_{idx}'].plot()

df.filter(like='cum_ret_').plot(legend=False)

#%%


#%%
# Some notes on log returns
# Using log returns we can harness benefits of compounding effects and 
# easiliy incorporota transaction cost in this case it is rebalancing cost

#%%


#%%
# Baseline portfolio allocation with the volatility targeting
#
# - Initial allocation is equally weighted
# - Adjust weights based on the volatility of security
# - Rebalancing will be done in weekly basis
#
#


#%%

rebalancing_cost   = 0.001 # 0.1% aka 10bps as rebalancing cost
volatility_window  = 45

returns            = df.filter(like='return_')
log_returns        = (1+returns).apply(np.log)
rolling_volatility = log_returns.rolling(window=volatility_window).std()
rolling_volatility = rolling_volatility.ewm(span=5, adjust=False, min_periods=5).mean() # Fast EMA5 smoothing for volatility

weekly_log_returns = log_returns.resample('W').sum()

weights            = np.ones(num_securities)/num_securities # weights shape is (num_securities,0)
portfolio_returns  = pd.DataFrame(index=weekly_log_returns.index, columns=['Portfolio'])


#%%
rolling_volatility.plot(legend=False)
plt.title(f'{volatility_window} days volatility');

#%%
weekly_log_returns.plot(legend=False)

#%%


#%%
for i, week in enumerate(weekly_log_returns.index):
    if i==0:
        # initial rebalancing, no cost
        weekly_log_returns_this_week = weekly_log_returns.iloc[i]
        portfolio_returns_this_week  = np.dot(weekly_log_returns_this_week, weights)
        portfolio_returns.loc[week, 'Portfolio'] = portfolio_returns_this_week
        pass
    else:
        prev_portfolio_value = portfolio_returns.iloc[i-1]['Portfolio']

        #print(weekly_log_returns.iloc[i-1])
        # volatility targeting
        inverse_volatility = 1 / weekly_log_returns.iloc[i-1].std()
        #print(inverse_volatility)
        new_weights        = weights * inverse_volatility
        new_weights       /= new_weights.sum()

        #print(new_weights)
        # calculate transaction cost in log space
        log_transaction_cost = np.abs(np.log(new_weights) - np.log(weights)).sum() * rebalancing_cost
        #print(log_transaction_cost)


        weights = new_weights
        #print(weights)
        #print('-----------')

        pass
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

