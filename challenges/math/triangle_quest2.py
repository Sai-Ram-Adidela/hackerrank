"""
Title     : Triangle Quest 2
Subdomain : HackerRank/Python/Challenges/math
Domain    : Python
Author    : Sai Ram Adidela
Created   : 07 May 2018
"""
if __name__ == '__main__':
    for i in range(1, int(input())+1):
        print((10**i-1)**2//81)
# input = 5 ,range = 6
# for i=1 10**1-1 --> 9 ** 2 --> 81//81 --> 1
# for i=2 10**2-1 --> 99 ** 2 --> 9801//81 --> 121
# for i=3 10**3-1 --> 999 ** 2 --> 998001//81 --> 12321
# for i=4 10**4-1 --> 9999**2 --> 99980001//81 --> 1234321
# for i=5 10**5-1 --> 99999**2 --> 9999800001//81 --> 123454321
