string = input()
string_ls = string.split("#")
count = 0
for i in string:
    if i == "#":
        string_ls.append("#")
print("".join(string_ls))