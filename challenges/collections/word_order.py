"""
Title     : Word Order
Subdomain : HackerRank/Python/Challenges/Collections
Domain    : Python
Author    : Sai Ram Adidela
Created   : 22 May 2018
"""
from collections import OrderedDict

no = int(input())
d = OrderedDict()
for i in range(no):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(len(d))
for key in d:
    print(d[key], end=' ')
