'''
A palindrome is a word or phrase which reads the same in both
directions. Given below are some palindromic strings:
deed
level
Malayalam
Rats live on no evil star
Murder for a jar ofred rum
Write a program that defines a function ispalindrome( ) which checks
whether a given string is a palindrome or not. Ignore spaces and case
mismatch while checking for palindrome.
'''

def ispalindrome(s):
    t=s.lower()
    left=0
    right=len(t)-1

    while right >= left:
        if t[left]=='':
            left += 1
        if t[right]=='':
            right -= 1
        if t[left] != t[right]:
            return False
        left += 1
        right -= 1
    return True

print(ispalindrome('Malayalam'))
print(ispalindrome('Rats live on no evil star'))
print(ispalindrome('Murder for a jar of red rum'))