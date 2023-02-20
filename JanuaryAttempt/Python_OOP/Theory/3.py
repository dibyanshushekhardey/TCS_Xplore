class Employee:
    def __init__(self, name, id, age, gender):
        self.eid=id
        self.ename=name
        self.age=age
        self.gender=gender

class Organisation:
    def __init__(self, name, elist):
        self.oname=name
        self.elist=elist

    def addEmployee(self, id, name, age, gender):
        print("In addEmployee function")
        e=Employee(id, name, age, gender)
        self.elist.append(e)
        print("End addEmployee function")

    def viewEmployees(self):
        print("In View Employee function")
        for e in self.elist:
            print(e.eid)
            print(e.ename)
            print(e.age)
            print(e.gender)
        print("End View Employee function")
    
    def getEmployeeCount(self):
        print("In countEmployee function")
        print("END countEmployee function")
        return len(self.elist)

    def findEmployeeAge(self, id):
        print("In findEmployee function")
        age = -1
        for e in self.elist:
            if e.eid == id:
                age = e.age
                break
        print("End findEmployee function")
        return age

    def countEmployees(self, age):
        count = 0
        print("In countEmployee AGE WISE function")
        for e in self.elist:
            if e.age > age:
                count+= 1
        print("In countEmployee AGE WISE function")

        return count


if __name__=="__main__":
    employees = []
    o = Organisation('ABC', employees)
    n=int(input())
    for i in range(n):
        name = input()
        id = int(input())
        age = int(input())
        gender = input()
        o.addEmployee(name, id, age, gender)
    
    o.viewEmployees()

    print(o.getEmployeeCount())

    id=int(input())
    print(o.findEmployeeAge(id))

    age = int(input())
    print(o.countEmployees(age))
    