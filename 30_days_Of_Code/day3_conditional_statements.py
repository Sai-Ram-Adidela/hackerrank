"""
Title     : day3_conditional_statements
Subdomain : 30 days of code
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
"""
N = input().strip()

if not N.isdigit():
    print("Not Weird")
else:
    N = int(N)
    if N % 2 == 0:
        if 5 >= N >= 2:
            print("Not Weird")
        elif 20 >= N >= 6:
            print("Weird")
        elif N > 20:
            print("Not Weird")
    else:
        print("Weird")
