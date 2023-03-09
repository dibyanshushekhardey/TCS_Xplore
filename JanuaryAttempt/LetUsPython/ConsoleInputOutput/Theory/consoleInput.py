# receive full name
name=input('Enter full name: ')
# separate first name, middl ename, and surname
fname, mname, sname=input('Enter full name: ').split()

# multiple int values
n1, n2, n3 = input("Enter three values: ").split()
n1, n2, n3=int(n1), int(n2), int(n3)
print(n1+10, n2+20, n3+30)

# using list and split function
n1, n2, n3 = [int(n) for n in input("Enter three values: ").split()]
print(n1+10, n2+20, n3+30)

# using input to receive arbitrary number of values
numbers=[int(x) for x in input('Enter values: ').split()]
for n in numbers:
    print(n+10)

# input can be used to receove different types of values at a time
data=input('Enter name, age, salary: ').split()
name=data[0]
age=int(data[1])
salary=float(data[2])
