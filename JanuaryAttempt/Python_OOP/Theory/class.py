class Employee:
    #common base class for all
    empCount = 0

    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total employee: {}".format(Employee.empCount))

    def displayEmployee(self):
        print("Name: {} Salary: {}".format(self.name, self.salary))

emp1 = Employee("Zara", 2000)
emp1 = Employee("Manni", 5000)