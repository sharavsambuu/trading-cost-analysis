# Trading-cost-analysis

  The goal of this repo is to make sense of how trading cost impacted to trading strategies.
  Trading cost is crutial to develop more robust and more realistic strategies.



# Todo

  - Download signification amount of tick data from some FX brokers
    Analyze Half Spread Rate on all time history

  - Try to track bid ask spreads from random brokerages, and also crypto brokerages as well
    Maybe have to write some script to tracks from MT5 platform etc...

  - Try to estimate half spread rates and see their stats and come up with with number

  - Try to apply spread cost derived from half spread rates in backtesting, find out where can I
    apply it, on entry and exit prices or use it as general trading cost as percentage etc...

  - Estimate trading cost for single symbol in interactive brokers, make sure to include
    Select random strategy let's say RSI 
    Estimate slippage cost
    Estimate spread cost
    Estimate commisison cost
    



# Commission fee based trading cost analysis

  Mostly crypto markets like binance charge through commission fee which is certain percentage of total traded value.

  Experiment on how many BPS of slippage happened from signals generated on 1H

    crypto_rsi_slippage.py

  From the slippage experiment I estimated 0.5BPS is ideal for BTC 1H slippage and backtested with 0.04% commission

    btc_macross_backtesting.py

  Other backtesting method is to map signals from higher timeframe to timeframe with lower granularity like 1m timeframe

    btc_macross_backtesting_1m.py



# Spread based trading cost analysis

  FX brokers tend to charge through spreads

  FX slippage estimation experiment

    fx_rsi_slippage.py

  FX spread estimation experiment

    fx_spread.py

  Slippage and spread involved backtesting

    fx_macross_backtesting.py

  Spread involved backtesting on lower granularity

    fx_macross_backtesting_1m.py






# References

  - Spread Fees and Backtesting - Algo Trading Q&A | Ep 1

    https://www.youtube.com/watch?v=K5IghR15sRk

    
  - Are you using the right backtest spread?

    https://www.youtube.com/watch?v=I0W-DAskwvY


  - Position sizing for practitioners 

    https://quantfiction.com/2018/12/20/position-sizing-for-practitioners-part-3-a-portfolio-approach/


  - Some frame of reference for 4H timeframe

    https://twitter.com/pedma7/status/1691419485117599747
    https://twitter.com/ThePythonQuant/status/1691552227943416157


  - Modeling Transaction Costs for Algorithmic Strategies

    https://www.youtube.com/watch?v=2w48B3U87a8


  - What are transaction costs and how do they impact your algorithm’s performance

    https://www.youtube.com/watch?v=LAUKOjZvvQQ


  - Calculating Market Impact
  
    https://quantopian-archive.netlify.app/forum/threads/calculating-market-impact.html


  - Market Impact Model Notebook

    https://notebook.community/quantopian/research_public/notebooks/lectures/Market_Impact_Model/notebook


  - Modelling Transaction Costs and Market Impact

    https://bsic.it/modelling-transaction-costs-and-market-impact/


  - Market Impact: Empirical Evidence, Theory and Practice Emilio Said

    https://hal.science/hal-03668669v1/file/Market_Impact_Empirical_Evidence_Theory_and_Practice.pdf


  - Quants turn to machine learning to model market impact

    https://www.risk.net/asset-management/4644191/quants-turn-to-machine-learning-to-model-market-impact


  - Retaining Alpha: The Effect of Trade Size and Rebalancing Frequency on FX Strategy Returns

    https://www.econstor.eu/bitstream/10419/216539/1/cesifo1_wp8143.pdf


  - Contract specific trading cost and optimal execution strategy

    https://quantfiction.com/2019/08/17/contract-specific-trading-costs-and-optimal-execution-strategy/


    

# MetaTrader5 and Linux related stuffs

    - Install wine
    - Install python3.9 windows version
        https://www.python.org/downloads/windows/
    - Install MetaTrader5 windows version
    - https://www.mql5.com/en/docs/python_metatrader5/mt5copyticksfrom_py
    - It looks like mt5linux doesn't fully support windows native package MetaTrader5 so have to run some of python scripts through the python in the wine.
    - Install windows based requirements through wine
        wine python -m pip install -r requirements_win.txt
    - Run windows version of python 
        wine python win_half_spread_rate_exps.py
    








