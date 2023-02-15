#WAP to take input array from the user and find the second largest value in numeric array

arr = []
n = int(input("Enter the number of elements to be entered: "))
for i in range(0, n):
    ele = int(input())
    arr.append(ele)

if len(arr) < 2:
    print("Invalid input")
else:
    arr.sort()
    print("In array: ", arr)
    print("Second largest element in the array is {}".format(arr[-2]))