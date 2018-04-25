"""
Title     : euler002/Sum Of Even Fibonacci Series
Subdomain : ProjectEuler+
Domain    : Python
Author    : Sai Ram Adidela
Created   : 19 April 2018
"""


def fibonacci(m):
    a, b = 0, 1
    su = 0
    for _ in range(n - 1):
        a, b = b, a + b
        if a % 2 == 0 and a < m:
            su = su + a
    return su


t = int(input())

for _ in range(t):
    n = int(input())
    print(fibonacci(n))
