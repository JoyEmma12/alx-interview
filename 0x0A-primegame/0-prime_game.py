#!/usr/bin/python3
"""
Game of choosing Prime numbers froma set
"""

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(n+1) if primes[i]]

def isWinner(x, nums):
    def can_win(n, primes):
        dp = [False] * (n+1)
        dp[0] = False
        dp[1] = False

        for i in range(2, n+1):
            if i in primes:
                dp[i] = not dp[i-1]

        return dp[n]

    winners = {'Maria': 0, 'Ben': 0}

    for n in nums:
        if n == 1:
            winners['Ben'] += 1
        else:
            primes = sieve_of_eratosthenes(n)
            if can_win(n, primes):
                winners['Maria'] += 1
            else:
                winners['Ben'] += 1

    max_wins = max(winners.values())

    if list(winners.values()).count(max_wins) == 1:
        return max(winners, key=winners.get)
    else:
        return None
