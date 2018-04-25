"""
Title     : Finding the Percentage
Subdomain : Challenges/Basic Data Types
Domain    : Python
Author    : Sai Ram Adidela
Created   : 23 April 2018
"""
if __name__ == '__main__':
    n = int(input())
    ls = list()
    my_dict = dict()
    for i in range(n):
        a = input()
        ls = a.split()
        d = ls[0]
        ls.remove(ls[0])
        newls = list(map(float, ls))
        my_dict[d] = newls
    name = input()
    total = 0
    if name in my_dict:
        marks = my_dict[name]
        no = len(marks)
        for num in marks:
            total += num
        avg = total / no
        print("%.2f" % avg)
