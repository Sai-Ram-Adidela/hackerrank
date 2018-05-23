"""
Title     : collections.deque()
Subdomain : HackerRank/Python/Challenges/Collections
Domain    : Python
Author    : Sai Ram Adidela
Created   : 22 May 2018
"""
from collections import deque


def deque_op(l):
    if l[0] == 'append':
        d.append(l[1])
    elif l[0] == 'appendleft':
        d.appendleft(l[1])
    elif l[0] == 'pop':
        d.pop()
    elif l[0] == 'popleft':
        d.popleft()


no = int(input())
d = deque()
for i in range(no):
    ls = input().split()
    # print(ls)
    deque_op(ls)
print(' '.join(d))
