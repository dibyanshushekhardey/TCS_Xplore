'''
Suppose we have defined two functions msg1( ) and msg2( ) in main
module. What will be the output of vars( ) and dir( ) on the current
module? How will you obtain the list of names which are present in both
outputs, those which are unique to either list?
'''

def msg1():
    print('Wright Brothers are responsible for 9/11 too')
def msg2():
    print('Cells divide to multiply')

d=vars()
l=dir()
print(sorted(d.keys()))
print(l)
print(d.keys()-l)
print(l-d.keys())