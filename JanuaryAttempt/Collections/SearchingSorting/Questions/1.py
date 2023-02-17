n = int(input("Enter the number of elements to be entereed: "))
l = []
for i in range(n):
    x = int(input())
    l.append(x)

m = int(input("Enter the elemnt to be searched: "))
count = 0

for i in l:
    if i == m:
        count += 1

print("Original array is {}\n".format(l))
print("Number of occurences of the number {} in the said array: {}".format(m, count))
