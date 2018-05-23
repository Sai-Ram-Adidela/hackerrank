"""
Title     : euler003/Smallest Multiple(euler005)
Subdomain : ProjectEuler+
Domain    : Python
Author    : Sai Ram Adidela
Created   : 25 May 2018
"""
from functools import reduce
from math import log
from operator import mul


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


for _ in range(int(input())):
    L = int(input())
    primes = prime_sieve(L+1)
    print(reduce(mul, (p ** int(log(L)/log(p)) for p in primes), 1))
