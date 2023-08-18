#!/usr/bin/python3
"""Program that returns an integer"""


def minOperations(n):
    """
    Returns an integer if n is impossible to achieve
    """
    if n == 1:
        return 0
        count = 1
        operations = 1

        while count < n:
            if count * 2 <= n:
                count *= 2
                operations += 1
                else:
                    count += 1
                    operations += 1

                return operations
