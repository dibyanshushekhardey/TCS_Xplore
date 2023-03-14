'''
Write a program to receive three integers from keyboard and get their
sum and product calculated through a user-defined function
cal_sum_prod( )
'''

def cal_sum_prod(x, y, z):
    ss=x+y+z
    pp=x*y*z
    return ss, pp

a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
s, p=cal_sum_prod(a, b, c)
print(s, p)