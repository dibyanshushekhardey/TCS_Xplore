string = input("Enter the value to add\n")
ls = string.split(" ")

# map
ls = list(map(lambda x:int(x),ls))
print(sum(ls))