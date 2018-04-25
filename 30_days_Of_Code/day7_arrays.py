"""
Title     : day7_Arrays
Subdomain : 30 days of code
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
"""
n = int(input())
arr = [i for i in input().strip().split(' ')]
# print(arr)
# s = ' '.join(arr)
# print(s)
# srev = ''.join(s[::-1])
# print(srev)
rarr = map(str, arr[::-1])
print(' '.join(rarr))
