def dec_to_oct(n):


n = int(input())

for i in range(1, n):
    print(i+' '+dec_to_oct(i)+' '+dec_to_hex(i)+' '+dec_to_bin(i))