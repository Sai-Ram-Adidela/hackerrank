"""
Title     : Set .difference()
Subdomain : HackerRank/Python/Challenges/sets
Domain    : Python
Author    : Sai Ram Adidela
Created   : 30 April 2018
"""

if __name__ == "__main__":
    eng_no = int(input())
    eng_roll = set(map(int, input().split()))

    fre_no = int(input())
    fre_roll = set(map(int, input().split()))

    ls = eng_roll.difference(fre_roll)  # or
    # ls = eng_roll - fre_roll
    print(len(ls))
