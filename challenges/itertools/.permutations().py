"""
Title     : itertools.permutations()
Subdomain : HackerRank/Python/Challenges/itertools
Domain    : Python
Author    : Sai Ram Adidela
Created   : 08 May 2018
"""
from itertools import permutations
if __name__ == '__main__':
    b = input().split()
    s = b[0]
    s = s.upper()
    k = int(b[1])
    ls = sorted(list(permutations(s, k)))
    for i in ls:
        print(''.join(i))
