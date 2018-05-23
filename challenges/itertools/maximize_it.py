"""
Title     : Maximize it
Subdomain : HackerRank/Python/Challenges/itertools
Domain    : Python
Author    : Sai Ram Adidela
Created   : 09 May 2018
"""


def maximize(l):
    su = 0
    for j in l:
        su += j*j
    print("total sum: ", su)
    print("value of M is: ", M)
    print(su % M)


if __name__ == '__main__':
    K, M = map(int, input().split())
    ls = list()
    max_no_ls = list()
    for i in range(K):
        ls = list(map(int, input().split()))
        print('given list ', ls, 'on ', i+1, 'th iteration')
        print(max(ls), ' in ', ls)
        max_no_ls.append((max(ls)))
    print('max num list: ', max_no_ls)
    maximize(max_no_ls)
