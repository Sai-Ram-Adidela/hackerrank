"""
Title     : day6_lets_review
Subdomain : 30 days of code
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
"""
n = int(input())


def odd_string(string):
    return string[1::2]


def even_string(string):
    return string[0::2]


o = e = ''
for i in range(0, n):
    s = input()
    o = odd_string(s)
    e = even_string(s)
    print(e+' '+o)
