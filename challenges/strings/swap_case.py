"""
Title     : Swap Case
Subdomain : Challenges/Strings
Domain    : Python
Author    : Sai Ram Adidela
Created   : 18 April 2018
"""


def swap_case(s):
    a = ''
    for i in s:
        if i.isupper():
            i = i.lower()
            a = a + i
        elif i.islower():
            i = i.upper()
            a = a + i
        else:
            a = a + i
    return a


if __name__ == '__main__':
    string = 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'
    result = swap_case(string)
    print(result)
