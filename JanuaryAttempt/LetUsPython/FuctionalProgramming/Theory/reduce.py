from functools import reduce

def getsum(x, y):
    return x+y
def getprod(x, y):
    return x*y

lst=[1, 2, 3, 4, 5]
s=reduce(getsum, lst)
p=reduce(getprod, lst)
print(s)
print(p)