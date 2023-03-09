'''
Write a program that prints square root and cube root of numbers from
1 to 10, up to 3 decimal places. Ensure that the output is displayed in
separate lines, with number center-justified and square and cube roots,
right-justified.
'''

import math
width = 10
precision = 4
for n in range(1, 10):
    s=math.sqrt(n)
    c=math.pow(n, 1/3)
    print(f'{n:^5}{s:{width}.{precision}}{c:{width}.{precision}}')