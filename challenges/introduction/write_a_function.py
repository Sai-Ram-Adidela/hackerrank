"""
Title     : Write a Function
Subdomain : HackerRank/Python3/Challenges/Introduction
Domain    : Python
Author    : Sai Ram Adidela
Created   : 23 April 2018
"""


def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap


y = int(input())
print(is_leap(y))
