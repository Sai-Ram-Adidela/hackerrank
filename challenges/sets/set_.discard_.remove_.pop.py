"""
Title     : Set .discard(), .remove() & .pop()
Subdomain : HackerRank/Python/Challenges/sets
Domain    : Python
Author    : Sai Ram Adidela
Created   : 30 April 2018
"""

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    no = int(input())
    ls = []

    for _ in range(no):
        ls = list(input().split())
        # ls.append(input().split())
        # print(ls[0])

        if ls[0] == 'pop':
            # print("this is pop")
            s.pop()
        elif ls[0] == 'remove':
            # print("this is remove")
            s.remove(int(ls[1]))
        elif ls[0] == 'discard':
            # print("this is discard")
            s.discard(int(ls[1]))

    # print(s)
    print(sum(s))
