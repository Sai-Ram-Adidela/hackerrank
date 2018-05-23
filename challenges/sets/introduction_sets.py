"""
Title     : Introduction to Sets
Subdomain : HackerRank/Python/Challenges/sets
Domain    : Python
Author    : Sai Ram Adidela
Created   : 20 April 2018
"""


def average(array):
    s = set(array)
    ls = list(s)
    total = sum(ls)
    count = len(ls)
    # print("set: ",s)
    # print("list: ",ls)
    # print("total sum: ",total)
    # print("length of list: ",count)
    return total/count


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
