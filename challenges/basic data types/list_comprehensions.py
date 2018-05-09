"""
Title     : List Comprehensions
Subdomain : HackerRank/Python3/Challenges/Basic Data Types
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    my_list = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(my_list)
