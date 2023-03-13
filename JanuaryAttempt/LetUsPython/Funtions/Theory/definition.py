# function definition
def fun():
    print('My opinions may have changed')
    print('But not the fact that I am right')

fun()
fun()

# nesting functions
def fun1():
    print("Reached fun1")
    def fun2():
        print('Inner avatar')
    print('Outer avatar')
    fun2()

fun1()
#fun2()
print(type(fun1()))