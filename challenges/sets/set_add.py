"""
Title     : Set .add()
Subdomain : HackerRank/Python/Challenges/sets
Domain    : Python
Author    : Sai Ram Adidela
Created   : 30 April 2018
"""

if __name__ == '__main__':
    n = int(input())
    s = set()
    for _ in range(n):
        s.add(input())
    print(len(s))
