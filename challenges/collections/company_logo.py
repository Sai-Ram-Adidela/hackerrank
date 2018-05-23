"""
Title     : Company Logo
Subdomain : HackerRank/Python/Challenges/Collections
Domain    : Python
Author    : Sai Ram Adidela
Created   : 22 May 2018
"""
from collections import Counter

s = sorted(input().strip())
s_counter = Counter(s).most_common()
s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
for i in range(0, 3):
    print(s_counter[i][0], s_counter[i][1])
