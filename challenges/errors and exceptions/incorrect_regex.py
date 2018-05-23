"""
Title     : Incorrect Regex
Subdomain : HackerRank/Python/Challenges/Errors and Exceptions
Domain    : Python
Author    : Sai Ram Adidela
Created   : 23 May 2018
"""
import re

no = int(input())
for _ in range(no):
    try:
        re.compile(input())
        print('True')
    except:
        print('False')
