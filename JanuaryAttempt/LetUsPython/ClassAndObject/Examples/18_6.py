'''
Is there any difference in the values returned by the functions dir( ) and
vars(..).keys( )? If yes, write a program to obtain that difference?
'''

s=set(dir(list)).difference(vars(list).keys())
print(s)