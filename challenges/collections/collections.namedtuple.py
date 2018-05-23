"""
Title     : collections namedtuple.
Subdomain : HackerRank/Python/Challenges/Collections
Domain    : Python
Author    : Sai Ram Adidela
Created   : 16 May 2018
"""
# from __future__ import division
from collections import namedtuple
no = int(input())
columns = ','.join(input().split())
# print('intial columns: ', columns)
student = namedtuple('student', columns)
sum = 0
for i in range(no):
    line = input().split()
    stu = student(*line)
    # print('stu: ', stu)
    sum += int(stu.MARKS)
print(sum/no)
