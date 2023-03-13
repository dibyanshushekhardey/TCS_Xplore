'''
Suppose a dictionary contains following information for 5 employees:
emp = {
'A101' : {'name' : 'Ashish', 'age' : 30, 'salary' : 21000},
'B102' : {'name' : 'Dinesh', 'age' : 25, 'salary' : 12200},
'A103' : {'name' : 'Ramesh', 'age' : 28, 'salary' : 11000},
'D104' : {'name' : 'Akheel', 'age' : 30, 'salary' : 18000},
'A105' : {'name' : 'Akaash', 'age' : 32, 'salary' : 20000}
}
Using dictionary comprehensions, write a program to create:
- Dictionary of all those codes and values, where codes that start with
'A'.
- Dictionary of all codes and names.
- Dictionary of all codes and ages.
- Dictionary of all codes and ages, where age is more than 30.
- Dictionary of all codes and names, where names start with 'A'.
- Dictionary of all codes and salaries, where salary is in the range
13000 to 20000.
'''
emp = {
'A101' : {'name' : 'Ashish', 'age' : 30, 'salary' : 21000},
'B102' : {'name' : 'Dinesh', 'age' : 25, 'salary' : 12200},
'A103' : {'name' : 'Ramesh', 'age' : 28, 'salary' : 11000},
'D104' : {'name' : 'Akheel', 'age' : 30, 'salary' : 18000},
}
d1={k:v for (k, v) in emp.items()if k.startswith('A')}
d2={k:v['name'] for (k, v) in emp.items()}
d3={k:v['age'] for (k, v) in emp.items()}
d4={k:v['age'] for (k, v) in emp.items() if v['age'] > 30}
d5={k:v['name'] for (k, v) in emp.items() if v['name'].startswith('A')}
d6={k:v['salary'] for (k, v) in emp.items() if v['salary'] > 13000 and v['salary'] <= 20000}
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)