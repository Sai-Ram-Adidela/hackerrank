"""
Title     : Set Mutations
Subdomain : HackerRank/Python/Challenges/sets
Domain    : Python
Author    : Sai Ram Adidela
Created   : 2 May 2018
"""
if __name__ == "__main__":
    set_no = int(input())
    a = set(map(int, input().split()))
    ope = int(input())
    result = int()

    for _ in range(ope):
        ls = list(input().split())
        ls1 = set(map(int, input().split()))

        if ls[0] == 'intersection_update':
            a.intersection_update(ls1)
            # print("intersection_update: ",a)
            result = sum(a)

        elif ls[0] == 'update':
            a.update(ls1)
            # print("update: ",a)
            result = sum(a)

        elif ls[0] == 'symmetric_difference_update':
            a.symmetric_difference_update(ls1)
            # print("symmetric_difference_update: ",a)
            result = sum(a)

        elif ls[0] == 'difference_update':
            a.difference_update(ls1)
            # print("difference_update: ",a)
            result = sum(a)
    print(result)
