"""
Title     : Detecting Floating Point Number
Subdomain : HackerRank/Python3/Challenges/Regex and Parsing
Domain    : Python3
Author    : Sai Ram Adidela
Created   : 23 Sep 2019
"""
import re

def verify_float(no):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', no)))

if __name__ == '__main__':
    cas = int(input())
    for t in range(cas):
        no = input()
        verify_float(no)
