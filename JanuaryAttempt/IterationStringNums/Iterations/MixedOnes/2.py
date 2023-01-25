# write a program to check if a string starts or end with given string
str = input()
pattern = input()
if (str.lower().startswith(pattern.lower()) or str.lower().endswith(pattern.lower())):
    print("{} contains {}".format(str, pattern))
else:
    print("{} does not contain {}".format(str, pattern))