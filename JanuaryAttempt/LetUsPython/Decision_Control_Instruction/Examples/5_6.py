'''
Given a number n we wish to do the following:
If n is positive - print n * n, set a flag to true
If n is negative - print n * n * n, set a flag to true
if n is 0 - do nothing
Is the code given below correct for this logic?
n = int(input('Enter a number: '))
if n > 0 :
flag = True
print(n * n)
elif n < 0 :
flag = True
print(n * n * n)
'''
n=int(input("Enter a number: "))
if n > 0:
    flag=True
    print(n*n)
elif n < 0:
    flag = True
    print(n*n*n)
else:
    pass