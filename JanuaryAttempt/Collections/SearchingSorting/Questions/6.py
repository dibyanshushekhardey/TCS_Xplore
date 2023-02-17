n = int(input("Student count: "))
l1 = []
for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter roll no: "))
    p = int(input("Enter no. of subjects: "))
    l = []
    for j in range(p):
        marks = int(input("Enter marks: "))
        l.append(marks)
    my_tuple = (name, roll, p, l)
    l1.append(my_tuple)
print(tuple(l1))