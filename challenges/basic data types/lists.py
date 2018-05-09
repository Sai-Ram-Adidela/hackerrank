"""
Title     : Lists
Subdomain : HackerRank/Python3/Challenges/Basic Data Types
Domain    : Python
Author    : Sai Ram Adidela
Created   : 23 April 2018
"""

if __name__ == '__main__':
    N = int(input())
    L = []

    for i in range(0, N):
        tokens = input().split()

        if tokens[0] == 'insert':
            L.insert(int(tokens[1]), int(tokens[2]))
        elif tokens[0] == 'print':
            print(L)
        elif tokens[0] == 'remove':
            L.remove(int(tokens[1]))
        elif tokens[0] == 'append':
            L.append(int(tokens[1]))
        elif tokens[0] == 'sort':
            L.sort()
        elif tokens[0] == 'pop':
            L.pop()
        elif tokens[0] == 'reverse':
            L.reverse()
