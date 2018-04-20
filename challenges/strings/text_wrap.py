"""
Title     : Text Wrap
Subdomain : Challenges/Strings
Domain    : Python
Author    : Sai Ram Adidela
Created   : 20 April 2018
"""
import textwrap


def wrap(s, width):
    k = ''
    ls = textwrap.wrap(s, width)
    for i in range(len(ls)):
        k = k + ls[i] + '\n'
    return k


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
