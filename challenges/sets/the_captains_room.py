"""
Title     : The Captains Room
Subdomain : HackerRank/Python/Challenges/sets
Domain    : Python
Author    : Sai Ram Adidela
Created   : 04 May 2018
"""
K = int(input())
nums = map(int, input().split())
nums = sorted(nums)
for i in range(1, len(nums)):
    if i != len(nums)-1:
        if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
            print(nums[i])
            break
    else:
        print(nums[i])
