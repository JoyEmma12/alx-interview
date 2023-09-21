#!/usr/bin/python3
"""
Determine fewest number of coins needed to meet total
return 0 total if total is 0 or less
else return -1
"""


def makeChange(coins, total):

    if total <= 0:
        return 0

    # Initialize a list to store the minimum
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        for amount in range(coin, total + 1):
            # Update the minimum number of coins needed for the current amount
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
