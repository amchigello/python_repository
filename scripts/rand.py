import time
import math

def lcg(modulus, a, c, seed):
    seed = (a * seed + c) % modulus
    return seed
    
for i in range(10):
    t=time.time()
    x=lcg(4,10,i,t)
    dec,num=math.modf(x)
    print(int(str(dec).replace('.','')))
