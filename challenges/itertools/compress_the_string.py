"""
Title     :  itertools.groupby()
Subdomain : HackerRank/Python/Challenges/itertools
Domain    : Python
Author    : Sai Ram Adidela
Created   : 08 May 2018
"""
from itertools import groupby
s = input()
groups = []
# s = sorted(s)
for k, g in groupby(s):
    groups.append((len(list(g)), int(k)))      # Store group iterator as a list

# print("groups: ", groups)
for i in groups:
    print(i, end=' ')
