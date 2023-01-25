# program to read an integer and check if i is a palindrome number
x = int(input())

if str(x)[::-1] == str(x):
    print("True")
else:
    print("False")
