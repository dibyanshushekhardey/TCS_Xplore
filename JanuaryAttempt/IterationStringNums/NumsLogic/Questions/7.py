# WAP to read a sentence and a word from console.
# Print the total number of occurences of the word in the following format:
# "The word 'x' appears 'y' times"
# Replace x with the intended word and y woth count of the word in the sentence

n = input()
word = input()

l = n.split()
count = 0
if word in l:
    count += 1
print("The wprd '{}' appears {} times".format(word, count))