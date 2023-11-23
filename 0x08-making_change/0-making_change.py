#!/usr/bin/python3
"""Change challenge
"""


def makeChange(coins, total):
    """  determine the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0
    memory = total
    i = 0
    coin_count = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while memory > 0:
        if i >= n:
            return -1
        if memory - sorted_coins[i] >= 0:
            memory -= sorted_coins[i]
            coin_count += 1
        else:
            coin_idx += 1
    return coin_count
