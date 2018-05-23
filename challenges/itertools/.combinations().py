"""
Title     : itertools.combinations()
Subdomain : HackerRank/Python/Challenges/itertools
Domain    : Python
Author    : Sai Ram Adidela
Created   : 08 May 2018
"""
from itertools import combinations, chain
if __name__ == '__main__':
    b = input().split()
    s = sorted(b[0].upper())
    k = int(b[1])
    ls = list()
    for i in range(1, k + 1):
        ls.append(sorted(list(combinations(s, i))))
    merged_ls = list(chain(*ls))
    for i in merged_ls:
        print(''.join(i))
