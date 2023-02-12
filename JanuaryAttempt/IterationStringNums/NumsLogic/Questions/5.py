# WAP to read a number from the console and write the sum of theor digits
n = input()

l = [int(x)for x in n]
sum = sum(l)
print(sum)