# Trading-cost-analysis

The goal of this repo is to make sense of how trading cost impacted to trading strategies.
Use simple RSI based strategy with exit and reverse mode.
Why? Because trading cost is crutial to develop more robust and more realistic strategies, that's why.


# Spread based trading cost analysis related tasks

  - Find FX data with 1minute granularity, mbe EURUSD or USDJPY
  - Find spread commission value from common FX brokers in order to estimate spread cost
  - Try to estimate BID and ASK spreads using rolling average
  - Estimated the BPS cost from the rolling spread averages.
  - Develop 1h based RSI strategy for FX with exit and reverse mode, starting cash is $100K
  - Map 1h signals to 1m timeframe for FX
  - Do analysis for slippage by BPS, make sure to include sensitivity test by discretized sigmas
  - Do analysis for spread impact, and also include sensitivity by discretized sigmas
  - Combine spread cost with slippage cost and extract final equity in dollar term
  - Do Monte-Carlo Simulation and extract common metrics like risk of ruin, DSR
  - Calculate maximum drawdown from the simulations
  - Use Position sizing based on maximum drawdown, generate dollar based equity again
  - Compare RSI strategy with or without trading cost involved
  

# Commission fee based trading cost analysis related tasks

  - Find Crypto data with 1minute granularity
  - Find taker fee value by bps from common crypto brokers in order to estimate commission cost
  - Develop 1h based RSI strategy for Crypto with exit and reverse mode, starting cash is $100K
  - Map 1h signals to 1m timeframe for Crypto
  - Do analysis for slippage by BPS, include sensitivity test by discretized sigmas
  - Combine commission fee cost with slippage by BPS cost and extract dollar based equity
  - Do Monte-Carlo Simulation and extract metrics like risk of ruin and DSR
  - Calculate maximum drawdown from the simulations
  - Use Position sizing based on maximum drawdown, generate dollar based equity again
  - Compare RSI strategy with or without trading cost involved


# Miscs


# References

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

    








