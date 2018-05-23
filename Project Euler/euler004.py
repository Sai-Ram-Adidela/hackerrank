"""
Title     : euler003/Largest Palindrome Product(euler004)
Subdomain : ProjectEuler+
Domain    : Python
Author    : Sai Ram Adidela
Created   : 25 May 2018
"""


def is_palindromic(n):
    n = str(n)
    return n == n[::-1]


def largest(l):
    pmax = 0
    for i in range(999, 100, -1):
        for j in range(990, 100, (-11 if i % 11 else -1)):
            p = i * j
            if p < pmax:
                break
            if p < l and is_palindromic(p):
                x, y, pmax = i, j, p
    if pmax > 0:
        print("%6d" % pmax)
    else:
        print('None Found')


for _ in range(int(input())):
    largest(int(input()))
