"""
Title     : itertools.product()
Subdomain : HackerRank/Python/Challenges/itertools
Domain    : Python
Author    : Sai Ram Adidela
Created   : 08 May 2018
"""
from itertools import product
if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ls = list(product(A, B))
    for i in ls:
        print(i, end=' ')
