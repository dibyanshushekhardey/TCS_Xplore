# WAP to search how many numbers in a given array are divisible by input value.
# also display those numbers

import array as arr

count = 0
lst = []
a = arr.array('i', [10, 20, 34, 57, 33, 21, 30])
ele = int(input("Enter element for divisibility:"))

for i in range(len(a)):
    if a[i] % ele == 0:
        count+=1
        lst.append(a[i])

print("Array is: ", end=" ")
for i in range(0, len(a)):
    print(a[i], end=" ")

print("\n", count, "Elements in array are divisible by", ele, "which are:", lst)