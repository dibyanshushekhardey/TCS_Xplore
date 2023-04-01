import random
# generate 20 random numbers in the range 10 to 100
# and obtain maximum out of them
print(max(random.randint(10, 100) for n in range(20)))
# print sum of cubes of all numberd less than 20
print(sum(n*n*n for n in range(20)))