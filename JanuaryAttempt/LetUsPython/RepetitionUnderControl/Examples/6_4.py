'''
Write a program that obtains decimal value of a binary numeric string.
For example, decimal value of '1111' is 15.
'''

b = '1111'
i = 0
while b:
    i = i *2 + (ord(b[0]) - ord('0'))
    b = b[1:]
print('Decimal value = '+str(i))