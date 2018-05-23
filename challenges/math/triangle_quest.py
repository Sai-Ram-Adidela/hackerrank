"""
Title     : Triangle Quest
Subdomain : HackerRank/Python/Challenges/math
Domain    : Python
Author    : Sai Ram Adidela
Created   : 08 May 2018
"""
if __name__ == '__main__':
    # iam did this solution by using 'str' but hacker rank not accepting with 'str'
    # for i in range(1, int(input())):
        # print(str(i) * i)
    for i in range(1, int(input())):
        print(((10 ** i - 1) // 9) * i)
