'''
Write a program that nests function fun2( ) inside function fun1( ).
Create two variables by the name a in each function. Prove that they are
two different variables.
'''

def fun1():
    a=45
    print(a)
    print(id(a))

    def fun2():
        a=90
        print(a)
        print(id(a))

    fun2()
fun1()