"""
Title     : euler002/Sum Of Even Fibonacci Series
Subdomain : ProjectEuler+
Domain    : Python
Author    : Sai Ram Adidela
Created   : 19 April 2018
"""


def fib(limit):
    f1, f2 = 0, 1
    while f1 < limit:
        yield f1
        f1, f2 = f2, f1 + f2


no = int(input())
for i in range(0, no):
    print(sum(filter(lambda n: n % 2 == 0, fib(int(input())))))
