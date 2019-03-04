from functools import reduce
lst=list(range(5))
x=reduce(lambda x,y:x*y,lst)