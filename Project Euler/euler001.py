"""
Title     : euler001/Multiples of 3 and 5
Subdomain : ProjectEuler+
Domain    : Python
Author    : Sai Ram Adidela
Created   : 19 April 2018
"""


def su(n, k):
    d = n // k
    return k * (d * (d+1)) // 2


def euler1(n):
    return su(n, 3) + su(n, 5) - su(n, 15)


t = int(input().strip())
for i in range(t):
    N = int(input().strip())
    print(euler1(N - 1))  # below N
