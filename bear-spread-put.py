# Importing libaries
import numpy as np

# Function to find the put payoff
def put_payoff(strike_price, premium, underlying_price):
    return np.maximum(strike_price - underlying_price, 0) - premium

# Stock Price
underlying_price = 200

# placing a long put
strike_price_LP = 220
premium_LP = 10

# Placing a short put
strike_price_SP = 180
premium_SP = 8

# Payoff from the long put
LP_payoff =  put_payoff(strike_price_LP, premium_LP, underlying_price)

# Payoff from the short put
SP_payoff =  put_payoff(strike_price_SP, premium_SP, underlying_price)

# Payoff from the bear spread
bear_spread = LP_payoff + SP_payoff

print("Payoff from the long put: ", LP_payoff)
print("Payoff from the short put: ", SP_payoff)
print("Payoff from the bear spread: ", bear_spread)
