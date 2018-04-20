"""
Title     : Find a String
Subdomain : Challenges/Strings
Domain    : Python
Author    : Sai Ram Adidela
Created   : 20 April 2018
"""


def count_substring(s, sub_s):
    no = 0
    for i in range(len(s)):
        if s[i:].startswith(sub_s):
            no += 1
    return no


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
