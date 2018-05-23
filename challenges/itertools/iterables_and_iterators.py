"""
Title     : Iterables and Iterators
Subdomain : HackerRank/Python/Challenges/itertools
Domain    : Python
Author    : Sai Ram Adidela
Created   : 09 May 2018
"""
from itertools import combinations
if __name__ == '__main__':
    N = int(input())
    s = input().split()
    k = int(input())
    count, total = 0, 0
    # print('this before for-loop: ', list(combinations(s, k)))
    for i in combinations(s, k):
        count += 'a' in i
        # print('count is: ', count)
        total += 1
        # print('total is: ', total)
    print(count/total)
