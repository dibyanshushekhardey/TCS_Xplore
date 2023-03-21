def fun():
    a=45
    global b 
    b = 6.28
    print(locals())
    print(globals())

a = 20
b = 3.14
s = 'Aabra ka Daabra'
print(locals())
print(globals())
fun()