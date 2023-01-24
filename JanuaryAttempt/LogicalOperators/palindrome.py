# check whether a given string is a palindrome

a = input()
b = a[::-1]

if a == b:
    print("{} is a palindrome".format(a))
else:
    print("{} is not a palindrome".format(a))