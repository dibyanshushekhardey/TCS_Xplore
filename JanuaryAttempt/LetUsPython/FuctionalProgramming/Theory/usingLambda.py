# using lambda wiith map()
lst1=[5, 10, 15, 20, 25]
m=map(lambda n:n*n, lst1)
print(list(m))

# using lambda with filter()
lst2=[5, 10, 18, 27, 25]
f=filter(lambda n:n%5 == 0, lst2)
print(list(f))

# using lambda with reduce()
from functools import reduce
lst3=[1, 2, 3, 4, 5]
s=reduce(lambda x, y:x+y, lst3)
p=reduce(lambda x, y:x*y, lst3)
print(s, p)

def fun(n):
    return n > 1000

lst=[10, 20, 30, 40, 50]
l=filter(fun, map(lambda x:x*x, lst))
print(list(l))