'''
Windows stores time of creation of a file as a 2-byte number.
Distribution of different bits which account for hours, minutes and
seconds is as follows:
left-most 5 bits: hours
middle 6 bits - minute
right-most 5 bits - second / 2
Write a program to convert time represented by a number 26031 into
12:45:30.
'''

tm = 26031
hr = tm >> 11
min = (tm & 0b11111100000) >> 5
sec = (tm & 0b11111) * 2
print(str(hr)+':'+str(min)+':'+str(sec))
