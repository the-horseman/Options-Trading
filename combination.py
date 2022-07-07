# Importing Libaries
import numpy as np

# Placing a long put
def bear_spread(S0, K, r, sigma, T, n):
    dt = T/n
    u = np.exp(sigma*np.sqrt(dt))
    d = 1/u
    q = (np.exp(r*dt)-d)/(u-d)
    p = 1-q
    S = np.zeros((n+1, n+1))
    S[0, 0] = S0
    for i in range(n):
        for j in range(i+1):
            S[i+1, j] = u*S[i, j]
            S[i+1, j+1] = d*S[i, j]
    for i in range(n):
        for j in range(i+1):
            S[i+1, j] = max(S[i+1, j]-K, 0)
    return S[n, 0]

# Placing short put
def bull_spread(S0, K, r, sigma, T, n):
    dt = T/n
    u = np.exp(sigma*np.sqrt(dt))
    d = 1/u
    q = (np.exp(r*dt)-d)/(u-d)
    p = 1-q
    S = np.zeros((n+1, n+1))
    S[0, 0] = S0
    for i in range(n):
        for j in range(i+1):
            S[i+1, j] = d*S[i, j]
            S[i+1, j+1] = u*S[i, j]
    for i in range(n):
        for j in range(i+1):
            S[i+1, j] = max(S[i+1, j]-K, 0)
    return S[n, 0]

# getting total payoff
def total_payoff(S0, K, r, sigma, T, n):
    return bear_spread(S0, K, r, sigma, T, n) + bull_spread(S0, K, r, sigma, T, n)

# getting the price of the option
def price(S0, K, r, sigma, T, n):
    return total_payoff(S0, K, r, sigma, T, n)

# printing the answer
print(price(100, 100, 0.05, 0.2, 1, 100))