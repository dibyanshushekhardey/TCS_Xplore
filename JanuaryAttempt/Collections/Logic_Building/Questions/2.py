# WAP to read a list from input and print the average of all elements in the list
n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

sum = 0
for element in l:
    sum += element

print("Average of the list is {}".format(sum / n))