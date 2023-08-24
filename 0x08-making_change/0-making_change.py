#!/usr/bin/python3
""" Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total """
import sys


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    min_coins = sys.maxsize
    for i in range(len(coins)):
        if total % coins[i] == 0:
            return int(total / coins[i])
        else:
            tmp = int(total / coins[i])
            min_coins = min(min_coins, tmp + makeChange(coins[i + 1:],
                                                        total % coins[i]))
    return min_coins if min_coins != sys.maxsize else -1
