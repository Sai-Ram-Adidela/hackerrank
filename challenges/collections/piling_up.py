"""
Title     : Piling Up
Subdomain : HackerRank/Python/Challenges/Collections
Domain    : Python
Author    : Sai Ram Adidela
Created   : 22 May 2018
"""
from collections import deque
cas = int(input())
for t in range(cas):
    n = int(input())
    dq = deque(map(int, input().split()))
    possible = True
    element = (2**31)+1
    while dq:
        left_element = dq[0]
        right_element = dq[-1]
        if right_element <= left_element <= element:
            element = dq.popleft()
        elif left_element <= right_element <= element:
            element = dq.pop()
        else:
            possible = False
            break
    if possible:
        print('Yes')
    else:
        print('No')
