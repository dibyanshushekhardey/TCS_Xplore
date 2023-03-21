def fun():
    # name conflict. local a shadows out global a 
    a = 45
    # name conflict use global b
    global b
    b = 6.28

    # uses local a, global b abd s
    #m no need to define s as global since it is not being changed
    print(a, b, s)

# global identifiers
a = 20
b = 3.14
s='Aabra ka Daabra'
fun()
print(a, b, s)