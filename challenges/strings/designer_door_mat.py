"""
Title     : Designer Door Mat
Subdomain : Challenges/Strings
Domain    : Python
Author    : Sai Ram Adidela
Created   : 25 April 2018
"""


def designer_door_mat(n, m):
    for i in range(1, n, 2):
        print(str('.|.' * i).center(m, '-'))
    print('WELCOME'.center(m, '-'))
    for i in range(n-2, -1, -2):
        print(str('.|.' * i).center(m, '-'))


if __name__ == '__main__':
    N, M = map(int, input().split())
    designer_door_mat(N, M)
