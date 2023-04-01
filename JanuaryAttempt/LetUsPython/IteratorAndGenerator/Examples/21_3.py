'''
Write a program that uses dictionary comprehension to print sin, cos
and tan tables for angles ranging from 0 to 360 in steps of 15 degrees.
Write generator expressions to find the maximum value of sine and cos.
'''

import math
pi=3.14
sine_table={ang:math.sin(ang*pi/180) for ang in range(0, 360, 90)}
cos_table={ang:math.cos(ang*pi/180) for ang in range(0, 360, 90)}
tan_table={ang:math.tan(ang*pi/180) for ang in range(0, 360, 90)}
print(sine_table)
print(cos_table)
print(tan_table)
maxsin=max((math.sin(ang*pi/180) for ang in range(0, 360, 90)))
maxcos=max((math.cos(ang*pi/180) for ang in range(0, 360, 90)))
print(maxsin)
print(maxcos)