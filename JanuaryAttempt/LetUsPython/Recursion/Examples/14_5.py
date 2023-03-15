'''
A positive integer is entered through the keyboard; write a function to
find the binary equivalent of this number using recursion
'''

import sys

def dec_to_binary(n):
    r = n%2
    n = int(n/2)
    if n != 0:
        dec_to_binary(n)
    print(r, end='')

sys.setrecursionlimit(10 ** 6)
num = int(input('Enter the number: '))
print('The binary equivalent is: ')
dec_to_binary(num)