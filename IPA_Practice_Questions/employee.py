class Employee:
    def __init__(self, empName, empDesignation, empSalary, loan):
        self.empName=empName
        self.empDesignation=empDesignation
        self.empSalary=empSalary
        self.loan=loan

class Organisation:
    def __init__(self, empObj, loanType, maxDesignationAmount):
        self.empList=empObj