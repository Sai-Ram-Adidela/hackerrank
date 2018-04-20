"""
Title     : Tuples
Subdomain : Challenges/Basic Data Types
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
"""
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
