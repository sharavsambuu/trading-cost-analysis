# Trading-cost-analysis

The goal of this repo is to make sense of how trading cost impacted to trading strategies.
Use simple RSI based strategy with exit and reverse mode.
Why? Because trading cost is crutial to develop more robust and more realistic strategies, that's why.


# Spread based trading cost analysis related tasks

  - Find FX data with 1minute granularity, mbe EURUSD or USDJPY
  - Find spread commission value from common FX brokers in order to estimate spread cost
  - Develop 1h based RSI strategy for FX with exit and reverse mode, starting cash is $100K
  - Map 1h signals to 1m timeframe for FX
  - Do analysis for slippage by BPS
  - Do analysis for spread impact
  - Combine spread cost with slippage cost and extract final equity in dollar term
  - Do Monte-Carlo Simulation and extract common metrics like risk of ruin, DSR
  - Calculate maximum drawdown from the simulations
  - Use Position sizing based on maximum drawdown, generate dollar based equity again
  - Compare RSI strategy with or without trading cost involved
  

# Commission fee based trading cost analysis related tasks'

  - Find Crypto data with 1minute granularity
  - Find taker fee value by bps from common crypto brokers in order to estimate commission cost
  - Develop 1h based RSI strategy for Crypto with exit and reverse mode, starting cash is $100K
  - Map 1h signals to 1m timeframe for Crypto
  - Do analysis for slippage by BPS
  - Combine commission fee cost with slippage by BPS cost and extract dollar based equity
  - Do Monte-Carlo Simulation and extract metrics like risk of ruin and DSR
  - Calculate maximum drawdown from the simulations
  - Use Position sizing based on maximum drawdown, generate dollar based equity again
  - Compare RSI strategy with or without trading cost involved


# Miscs


