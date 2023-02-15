# Searcg numeric values from array between 
# given range of two input values 
# define a function to set logic to count in range

def countInRange(arr, n, x, y):
    count = 0
    for i in range(n):
        if arr[i] >= x and arr[i] <= y:
            count += 1
    return count

arr = []
n = int(input("Enter number of elements in array: "))
for i in range(0, n):
    ele = int(input())
    arr.append(ele)

arr_size = len(arr)
i = int(input("Enter range start point: "))
j = int(input("Enter range end point: "))

num = countInRange(arr, arr_size, i, j)
if num != 0:
    print("Values between {} and {} are {}".format(i, j, num))
else:
    print("No values found")