"""
Title     : Check Strict Superset
Subdomain : Challenges/sets
Domain    : Python
Author    : Sai Ram Adidela
Created   : 21 May 2018
"""
set_a = set(input().split())
n = int(input())
stmt = True
for _ in range(n):
    set_b = set(input().split())
    if not (set_b < set_a):
        stmt = False
        break
print(stmt)
