#!/usr/bin/python3
"""
minimum number of operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file.

    Args:
        n: The number of desired H characters.

    Returns:
        An integer representing the minimum number of operations needed to achieve n H characters.
    """
    steps = 0
    if n < 2:
        return 0
    for i in range(2, n + 1):
        while n % i == 0:
            n = n / i
            steps += i
    return steps
