# program to take 4 digit number and
# write the sum of its digits

n = int(input())
sum = 0

for i in str(n):
    sum += int(i)
print(sum)