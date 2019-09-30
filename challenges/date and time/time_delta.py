"""
Title     : Time Delta
Subdomain : HackerRank/Python3/Challenges/Date and Time
Domain    : Python3
Author    : Sai Ram Adidela
Created   : 23 Sep 2019
"""
import datetime

def time_delta(timestamp1, timestamp2):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time_second1 = datetime.datetime.strptime(timestamp1, time_format)
    time_second2 = datetime.datetime.strptime(timestamp2, time_format)
    print(int(abs((time_second1-time_second2).total_seconds())))

if __name__ == '__main__':
    cas = int(input())
    for t in range(cas):
        timestamp1 = input().strip()
        timestamp2 = input().strip()
        time_delta(timestamp1, timestamp2)
