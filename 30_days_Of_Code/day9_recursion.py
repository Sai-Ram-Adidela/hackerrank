"""
Title     : day9_Recursion
Subdomain : 30 days of code
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
"""


def factorial(no):
    # print("no is: ",no)
    # Complete this function
    if no == 1:
        return no
    else:
        return no * factorial(no-1)


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
