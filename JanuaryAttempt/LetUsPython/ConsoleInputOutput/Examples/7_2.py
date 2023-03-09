'''
Write a program to receive 3 integers using one call to input( ). The
three integers signify starting value, ending value and step value for a
range. The program should use these values to print the number, its
square and its cube, all properly right-aligned. Also output the same
values left-aligned.
'''

start, end, step = input('Enter start, end, step values: ').split()
# right aligned printing
for n in range(int(start), int(end), int(step)):
    print(f'{n:>5}{n**2:>7}{n**3:>8}')
print()

# left aligned printing
for n in range(int(start), int(end), int(step)):
    print('{0:<5}{1:<7}{2:<8}'.format(n, n**2, n**3))