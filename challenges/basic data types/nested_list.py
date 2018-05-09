"""
Title     : Nested List
Subdomain : HackerRank/Python3/Challenges/Basic Data Types
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
"""
if __name__ == '__main__':
    n = int(input())
    marksheet = [(input(), float(input())) for _ in range(n)]   # taking marks and names into one list.
    # print(marksheet)
    marks = [mark for name, mark in marksheet]                # separating only marks into other list.
    # print(marks)
    second_highest = sorted(set(marks))[1]                    # finding second highest value by sorted().
    # print(second_highest)
    names = [name for [name, mark] in marksheet if second_highest == mark]   # finding names which matches with the
    # second highest value, and that names all stored in one list.
    # print(names)
    print('\n'.join(sorted(names)))                           # printing lists by sorting.
