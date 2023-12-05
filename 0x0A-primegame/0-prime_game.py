#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    maria_count = 0
    ben_count = 0

    # generate primes between 1 and nums
    n = max(nums)
    primes = [True for i in range(1, n + 1)]
    primes[0] = False
    for i, a_prime in enumerate(primes, 1):
        if i == 1 or not a_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # fetch the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        prime_items = len(list(filter(lambda x: x, primes[0: n])))
        ben_count += prime_items % 2 == 0
        maria_count += prime_items % 2 == 1

    if maria_count == ben_count:
        return None
    return 'Maria' if maria_count > ben_count else 'Ben'
