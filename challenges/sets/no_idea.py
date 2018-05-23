"""
Title     : No Idea!
Subdomain : HackerRank/Python/Challenges/sets
Domain    : Python
Author    : Sai Ram Adidela
Created   : 23 May 2018
"""
n, m = (int(i) for i in input().split())
l = map(int, input().strip().split(' '))
a = set(map(int, input().strip().split(' ')))
b = set(map(int, input().strip().split(' ')))
result = 0
for i in l:
    if i in a:
        result += 1
    if i in b:
        result += -1
print(result)
