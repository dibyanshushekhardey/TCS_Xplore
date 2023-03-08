'''
Write a program that receives 3 sets of values of p, n and r and
calculates simple interest for each.
'''

i = 1
while i <= 3:
    p = float(input('Enter value of p: '))
    n = int(input("Enter value of n: "))
    r = float(input("Enter value of r: "))
    si = p * n * r /100
    print('Simple interest = Rs. '+str(si))
    i += 1