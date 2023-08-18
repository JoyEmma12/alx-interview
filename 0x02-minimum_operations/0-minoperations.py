#!/usr/bin/python3
"""Program that returns an integer"""


def minOperations(n):
    """
    Returns an integer if n is impossible to achieve
    """
    if n == 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i  # Initialize with the maximum possible value
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != n else 0
