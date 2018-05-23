"""
Title     : collections.OrderDict()
Subdomain : HackerRank/Python/Challenges/Collections
Domain    : Python
Author    : Sai Ram Adidela
Created   : 21 May 2018
"""
from collections import OrderedDict

items = list()

for i in range(int(input())):
    entry = input().strip().split()
    name = " ".join(entry[0:len(entry)-1])
    price = int(entry[len(entry)-1])
    items.append((name, price))

d = OrderedDict()
for item in items:
    try:
        d[item[0]] += item[1]
    except KeyError as e:
        d[item[0]] = item[1]

for item in d.items():
    print(item[0], item[1])
