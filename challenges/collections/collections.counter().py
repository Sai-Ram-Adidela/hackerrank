"""
Title     : collections.Counter()
Subdomain : HackerRank/Python/Challenges/Collections
Domain    : Python
Author    : Sai Ram Adidela
Created   : 15 May 2018
"""
from collections import Counter

no_of_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
no_of_customers = int(input())

total_money = 0

for i in range(no_of_customers):
    (size, price) = map(int, input().split())
    if shoe_sizes[size] > 0:
        shoe_sizes[size] -= 1
        total_money += price
print(total_money)
