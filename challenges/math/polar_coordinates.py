"""
Title     : Polar Coordinates
Subdomain : HackerRank/Python/Challenges/math
Domain    : Python
Author    : Sai Ram Adidela
Created   : 07 May 2018
"""
import cmath
if __name__ == '__main__':
    z = complex(input())
    print(abs(complex(z.real, z.imag)))
    print(cmath.phase(complex(z.real, z.imag)))
