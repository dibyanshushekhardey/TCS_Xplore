# Read a list from input
# find count of prime numbers in the list

n = int(input())

l= [] 

for i in range(n):
    l.append(int(input()))

prime_count = 0

for element in l:
    if element == 1 or element == 0:
        continue
    else:
        prime = True
        for number in range(2, element):
            if element % number == 0:
                print(False)
        if prime == True:
            prime_count += 1
print("There are {} prime numbers in list".format(prime_count))