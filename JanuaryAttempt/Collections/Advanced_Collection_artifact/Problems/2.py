data = input()
str = [i for i in data if i.isdigit() == False]
special = [i for i in str if i.isalpha() == False]
str = [i for i in str if i.isalpha() == True]
print("".join(str)+"".join(special))