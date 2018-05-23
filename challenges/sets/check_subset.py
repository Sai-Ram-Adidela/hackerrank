"""
Title     : Check Subset
Subdomain : Challenges/sets
Domain    : Python
Author    : Sai Ram Adidela
Created   : 04 May 2018
"""
no_of_test_cases = int(input())
for _ in range(no_of_test_cases):
    len_a = int(input())
    # print('length of a: ', len_a)
    ls_a = input().split()
    # print('list a: ', ls_a)
    set_a = set(ls_a)
    # print('set of a: ', set_a)
    len_b = int(input())
    # print('length of b: ', len_b)
    ls_b = input().split()
    # print('list b: ', ls_b)
    set_b = set(ls_b)
    # print('set of b: ', set_b)
    print(set_a < set_b)
