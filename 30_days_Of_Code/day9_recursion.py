'''
Title     : Recursion
Subdomain : 30 days of code
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
'''


def factorial(n):
    # print("n is: ",n)
    # Complete this function
    if n==1:
        return n
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
