n = int(input("Enter the number of elements to be entereed: "))
l = []
for i in range(n):
    x = int(input())
    l.append(x)

a = int(input("Enter range start value: "))
b = int(input("Enter range end value: "))

check_list = []

for i in range(a, b+1):
    check_list.append(i)

m = []
for ele in l:
    if ele in check_list:
        m.append(1)
    else:
        m.append(0)

if 0 in m:
    print("False")
else:
    print("True")