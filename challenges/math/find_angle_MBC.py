"""
Title     : Find Angle MBC
Subdomain : HackerRank/Python/Challenges/math
Domain    : Python
Author    : Sai Ram Adidela
Created   : 07 May 2018
"""
if __name__ == '__main__':
    import math
    AB = int(input())
    BC = int(input())
    print(str(round(math.degrees(math.atan2(AB, BC))))+'°')
