"""
Title     : euler003/Sum Square Difference(euler006)
Subdomain : ProjectEuler+
Domain    : Python
Author    : Sai Ram Adidela
Created   : 25 May 2018
"""


def su(num):  # sum_of_squares-->(1+2+3...)² ; squares_of_sum--> (1²+2²+3²...)
    sum_sum_of_squares = ((num * (num + 1)) // 2) ** 2
    sum_squares_of_sum = (num * (num + 1) * ((2 * num) + 1)) // 6
    return abs(sum_squares_of_sum - sum_sum_of_squares)


no = int(input())
for _ in range(no):
    k = int(input())
    print(abs(su(k)))
