"""
Title     : Runner Up Score
Subdomain : HackerRank/Python3/Challenges/Basic Data Types
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    # print("nor list: ",arr)
    arr.sort(reverse=True)
    print(arr[1])
