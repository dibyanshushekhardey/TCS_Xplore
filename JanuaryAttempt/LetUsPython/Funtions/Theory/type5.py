def print_it(i, j, *args, x, y, **kwargs):
    print()
    print(i, j, end='')
    for var in args:
        print(var, end='')
    print(x, y, end='')
    for name, value in kwargs.items():
        print(name, value, end='')

print_it(10, 20, x=30, y=40)
print_it(10, 20, 100, 200, x=30, y=40)
print_it(10, 20, 100, 200, y=40, x=30)        
print_it(10, 20, 100, 200, x=30, y=40, a=5, b=6, c=7)
#print_it(10, 20, 30, 40)

def fun(a, b=100, c=3.14):
    return a+b+c
w=fun(10)
x=fun(20, 50)
y=fun(30, 60, 6.28)
z=fun(1, c=3, b=5)