import time
import math


# x1 = ax0 +c (mod m)
# where x,a,c < m

def lcg(a, x0, c, modulus):
    x1 = ((a * x0) + c) % modulus
    return x1


for i in range(1, 20):
    x0 = i
    a = 2
    c = 5
    m = 50
    res = lcg(a, x0, c, m)
    print(res, end=" ")
