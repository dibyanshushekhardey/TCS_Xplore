'''
Write a program that proves that the dictionary returned by globals( )
can be used to manipulate values of variables in it.
'''

a=30
b=40
c=50
globals()['a']=25
globals()['b']=35
globals()['c']=45
print(a, b, c)