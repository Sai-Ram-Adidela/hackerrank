"""
Title     : itertools.combinations_with_replacement()
Subdomain : HackerRank/Python/Challenges/itertools
Domain    : Python
Author    : Sai Ram Adidela
Created   : 08 May 2018
"""
from itertools import combinations_with_replacement, chain
if __name__ == '__main__':
    b = input().split()
    s = sorted(b[0].upper())
    k = int(b[1])
    ls = list()
    ls.append(list(combinations_with_replacement(s, k)))
    # print(ls)
    ls = list(chain(*ls))
    # print(ls)
    for i in ls:
        print(''.join(i))
