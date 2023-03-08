'''
Write a program that prints numbers from 1 to 10 using an infinite loop.
All numbers should get printed in the same line.
'''

i = 1
while 1:
    print(i, end=' ')
    i += 1
    if i > 10:
        break