def sum(x, y, f):
    print(x+y)
    f()

def func():
    print('Hello')

f = func
sum(10, 20, f)