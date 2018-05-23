"""
Title     : Power - Mod Power
Subdomain : HackerRank/Python/Challenges/math
Domain    : Python
Author    : Sai Ram Adidela
Created   : 07 May 2018
"""
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    if m:
        if a >= 0 and b >= 0:
            print(pow(a, b))
            print(pow(a, b, m))
