"""
Title     : Alphabet Rangoli
Subdomain : Challenges/Strings
Domain    : Python
Author    : Sai Ram Adidela
Created   : 25 April 2018
"""
import string


def print_rangoli(k):
    mid = k - 1
    for i in range(k - 1, 0, -1):
        row = ['-'] * (2 * k - 1)
        for j in range(k - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))

    for i in range(0, k):
        row = ['-'] * (2 * k - 1)
        for j in range(0, k - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
