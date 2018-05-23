from itertools import product

K, M = map(int, input().split())

L = list()
ls = list()
for i in range(0, K):
    ls = list(map(int, input().split()))
    print('list ls before pop: ', ls)
    ls.pop(0)
    print('list ls after pop: ', ls)
    L.append(ls)
    print('list L: ', L)

ma = 0
pro_ls = list(product(L))
print('product() of L is: ', pro_ls)
for i in pro_ls:
    s = 0
    for j in i:
        s += pow(j, 2)
    r = s % M
    if r > ma:
        ma = r

print(ma)
