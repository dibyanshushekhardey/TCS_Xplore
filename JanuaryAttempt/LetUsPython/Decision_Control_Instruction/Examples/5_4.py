'''
A company insures its drivers in the following cases:
- If the driver is married.
- If the driver is unmarried, male & above 30 years of age.
- If the driver is unmarried, female & above 25 years of age.

In all other cases, the driver is not insured. If the marital status, sex and
age of the driver are the inputs, write a program to determine whether
the driver should be insured or not.
'''

ms = input('Enter marital status: ')
s=input("Enter sex: ")
age=int(input("Enter age: "))
if (ms == 'm') or (ms == 'u' and s == 'm' and age > 30) or (ms == 'u' and s == 'f' and age > 25):
    print('Insured')
else:
    print("Not Insured")