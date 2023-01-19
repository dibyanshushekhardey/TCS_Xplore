# write a python program to read a 4 digit integer value as an input and
# perform sum of all the digits of the input integer
# print the sum as shown in sample output

# take input
n = int(input())

# create a list to store individual digits
l = []

# append the digits
for i in str(n):
    l.append(i)

sum = 0

# summing performance
while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10

# final result
print("{}+{}+{}+{}={}".format(l[0], l[1], l[2], l[3], sum))