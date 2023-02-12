# WAP to read a word from console 
# Print the length of the longest repeating character streak
def longest(s):
    maximum = count = 0
    current = ''
    for c in s:
        if c == current:
            count += 1
        else:
            count = 1
            current = c
        maximum = max(count, maximum)
    return maximum

n = input()
print(longest(n))