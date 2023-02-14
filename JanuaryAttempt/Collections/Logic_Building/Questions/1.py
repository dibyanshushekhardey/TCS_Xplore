# WAP to read a list from input and print the ,minimum and maximum elements in list
n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

l.sort()

print("Maximum element is {}".format(l[-1]))
print("Minimum element is {}".format(l[0]))