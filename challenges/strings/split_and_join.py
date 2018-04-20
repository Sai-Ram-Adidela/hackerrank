"""
Title     : Split and Join
Subdomain : Challenges/Strings
Domain    : Python
Author    : Sai Ram Adidela
Created   : 20 April 2018
"""


def split_and_join(l):
    a = l.split(' ')
    a = '-'.join(a)
    return a


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
