# for a given string 'Bamboozled' write a program to obtain
# the following output

s='Bamboozled'

print(s[0], s[1])
print(s[-10], s[-9])

print(s[8], s[9])
print(s[2], s[-1])

print(s[2:10])
print(s[2:])
print(s[-8:])

print(s[0:6])
print(s[:6])
print(s[-10:-4])
print(s[:-4])

print(s[::-1])

print(s[0:10:1])
print(s[0:10:2])
print(s[0:10:3])
print(s[0:10:4])

s=s+'Hype!'
print(s)
s=s[:6]+'Monger'+s[-1]
print(s)