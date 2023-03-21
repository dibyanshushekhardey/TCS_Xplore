'''
Write a program that proves that if the dictionary returned by locals( ) is
manipulated, the values of original variables don't change.
'''

def fun():
    a=10
    b=20
    c=30
    locals()['a']=25
    locals()['b']=50
    locals()['c']=75
    print(a, b, c)

fun()