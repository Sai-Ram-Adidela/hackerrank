"""
Title     : Set Symmetric Difference
Subdomain : HackerRank/Python/Challenges/sets
Domain    : Python
Author    : Sai Ram Adidela
Created   : 2 May 2018
"""
if __name__ == '__main__':
    set1_n = int(input())
    set1 = set(map(int, input().split()))
    set2_n = int(input())
    set2 = set(map(int, input().split()))
    # print("set1: ",set1)
    # print("set2: ",set2)

    result = set1.symmetric_difference(set2)
    # print(type(result))
    # print("result: ",result)

    sorted_result = sorted(result)
    sorted_result = map(str, sorted_result)
    # print(type(sorted_result))
    # print("sorted_result: ",sorted_result)

    print('\n'.join(sorted_result))
