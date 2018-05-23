"""
Title     : Exceptions
Subdomain : HackerRank/Python/Challenges/Errors and Exceptions
Domain    : Python
Author    : Sai Ram Adidela
Created   : 23 May 2018
"""
no = int(input())
for _ in range(no):
    try:
        a, b = (int(x) for x in input().split())
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)
    except BaseException as e:
        print('Error Code:', e)
