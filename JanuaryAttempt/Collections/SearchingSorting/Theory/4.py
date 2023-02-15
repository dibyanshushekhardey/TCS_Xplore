# implement selection sort algorithm

my_list = []
n = int(input("Enter number of elements: "))

print("ENter list of elements: ")
for i in range(n):
    ele = int(input())
    my_list.append(ele)

print("Original list is:", my_list)

for x in range(len(my_list)):
    for y in range(x+1, len(my_list)):
        if my_list[x] > my_list[y]:
            temp = my_list[x]
            my_list[x] = my_list[y]
            my_list[y] = temp
            
print("Sorted list is: ", my_list)