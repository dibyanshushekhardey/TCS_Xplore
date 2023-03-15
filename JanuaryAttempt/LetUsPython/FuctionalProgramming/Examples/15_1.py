'''
Define three functions fun( ), disp( ) and msg( ), store them in a list and
call them one by one in a loop.
'''

def fun():
    print('In fun')

def disp():
    print('In msg')

def msg():
    print('In msg')

lst=[fun, disp, msg]
for f in lst:
    f()
