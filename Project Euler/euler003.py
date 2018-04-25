"""
Title     : euler003/Largest Prime Factor(euler003)
Subdomain : ProjectEuler+
Domain    : Python
Author    : Sai Ram Adidela
Created   : 19 April 2018
"""

import math


def max_prime_factors(n):
    maxprime = -1

    while n % 2 == 0:
        maxprime = 2
        n >>= 1  # equivalent to n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxprime = i
            n = n / i

    if n > 2:
        maxprime = n

    return int(maxprime)


t = int(input())
for _ in range(t):
    k = int(input())
    print(max_prime_factors(k))
