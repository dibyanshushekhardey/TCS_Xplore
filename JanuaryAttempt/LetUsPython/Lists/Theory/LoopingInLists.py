# while or for loop
animals = ['Zebra', 'Tiger', 'Lion', 'Jackal', 'Kangaroo']

# using whiule loop
i = 0
while i < len(animals):
    print(animals[i])
    i += 1

# using for loop
for a in animals:
    print(a)

# enumerate function
animals = ['Zebra', 'Tiger', 'Lion', 'Jackal', 'Kangaroo']
for index, a in enumerate(animals):
    print(index, a)