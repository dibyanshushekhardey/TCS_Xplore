'''
write a python program to take a string as 
input ans count the number of vowels in the string.
Your code is expected to print the count value as output
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
def countVowel(n):
    vowel=['a', 'e', 'i', 'o', 'u']
    m = list(n)
    count=0
    for i in m:
        if i.lower() in vowel:
            count += 1
    return count
text=input()
print(countVowel(text))