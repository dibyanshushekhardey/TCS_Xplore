# read a string from input and print the cpunt of esch vowels
sentence = input()
for char in ['a', 'e', 'i', 'o', 'u']:
    c = 0
    for letter in sentence:
        if letter.lower() == char:
            c += 1

    print("{} - {}".format(char, c))