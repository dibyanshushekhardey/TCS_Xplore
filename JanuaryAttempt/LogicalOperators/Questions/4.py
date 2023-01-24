Salary = float(input())
hike = 0
if Salary >= 10000:
    hike = 0.1 * Salary
elif Salary < 10000 and Salary >= 6000:
    hike = 0.08 * Salary
else:
    hike = 0.05 * Salary

Salary += hike
Salary = round(Salary, 2)
print(Salary)