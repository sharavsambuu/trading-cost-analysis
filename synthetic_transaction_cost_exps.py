#%%
import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt

#%%


#%%


#%%
# Preparing returns without transaction cost

num_periods  = 200

start_date   = pd.to_datetime('2022-01-01')
end_date     = pd.to_datetime('2023-12-31')
trade_dates  = pd.to_datetime(np.sort(np.random.choice(pd.date_range(start=start_date, end=end_date, periods=num_periods + 1), num_periods, replace=False)))

df = pd.DataFrame({'datetime'  : trade_dates})
df['datetime' ] = pd.to_datetime(df['datetime'])
df['datetime_'] = df['datetime']
df = df.set_index('datetime')

outliers_percentage = 30
outliers_percentage = outliers_percentage/100.0
outliers_count      = int(num_periods*outliers_percentage)

percentage_changes = np.random.uniform(-0.045, 0.05, num_periods).astype(float)
extreme_returns    = np.random.uniform(-0.03,  0.1, outliers_count).astype(float)
outliers_date      = df['datetime_'].sample(n=outliers_count).to_list()
df[f"return"]      = percentage_changes

for outlier in list(zip(outliers_date, extreme_returns)):
    outlier_dt  = outlier[0]
    outlier_ret = outlier[1]
    df.loc[outlier_dt, f"return"] = outlier_ret

df.drop('datetime_', axis=1, inplace=True)

df['cum_return_test'] = df['return'].cumsum()

df['cum_return_test'].plot()


#%%
df

#%%


#%%
# Applying different transaction costs

# 0.15% for the commission
# 0.2%  for the spread and slippage
commission_percentage      = 0.0015 # 0.15%
spread_slippage_percentage = 0.002  # 0.2%
transaction_cost_log_0     = np.log(1-commission_percentage) + np.log(1-spread_slippage_percentage)

# Applying transaction cost as 0.5%
transaction_cost_percentage = 0.005 # 0.5%
transaction_cost_log_1      = np.log(1-transaction_cost_percentage)

# Adjusting with the different transaction costs
df['log_return'           ] = (1 + df['return']).apply(np.log)
df['adjusted_log_return_0'] = df['log_return'] + transaction_cost_log_0 # commission 0.15%, slippage 0.2%
df['adjusted_log_return_1'] = df['log_return'] + transaction_cost_log_1 # single cost 0.5%


# cumulating returns 
df['cum_return'           ] = df['log_return'           ].cumsum().apply(np.exp)
df['adjusted_cum_return_0'] = df['adjusted_log_return_0'].cumsum().apply(np.exp)
df['adjusted_cum_return_1'] = df['adjusted_log_return_1'].cumsum().apply(np.exp)

df


#%%


#%%
df[['cum_return', 'adjusted_cum_return_0', 'adjusted_cum_return_1']].plot()
plt.legend(['strategy without cost', 'commission 0.15%, slippage 0.2%', 'estimated 0.5% cost'])



#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%


#%%

