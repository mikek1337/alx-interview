#!/usr/bin/env python3
""" Minimum Operations """


def minOperations(n):
    """ Minimum Operations """
    if n <= 1:
        return 0
    if n % 2 == 0:
        return int(minOperations(n / 2) + 2)
    else:
        return int(minOperations((n - 1) / 2) + 2)
