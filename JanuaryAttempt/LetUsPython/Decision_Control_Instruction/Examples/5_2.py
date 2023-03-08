'''
In a company an employee is paid as under:
If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary
and DA = 90% of basic salary. If his salary is either equal to or above Rs.
1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the employee's
salary is input through the keyboard write a program to find his gross
salary.
'''

bs=int(input("Enter value of bs: "))
if bs > 1000:
    hra=bs * 15/100
    da = bs * 95 / 100
    ca = bs * 10 / 100
else:
    hra = bs * 10 /100
    da = bs * 90 / 100
    ca = bs * 5 / 100
gs=bs+da+hra+ca
print("Gross Salary=Rs. "+str(gs))