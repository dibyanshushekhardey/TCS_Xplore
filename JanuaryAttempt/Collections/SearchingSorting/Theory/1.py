# WAP to search input value
# create a list by taking input frm the user.
# also check if the search value is numeric or string

lst = []
flag = 0
n = int(input("Enter the number of element to be enterered: "))

for i in range(0, n):
    ele = input()
    lst.append(ele)

search_ele = input("Enter element to be searched:")
for i in lst:
    if i == search_ele:
        flag += 1
if str(search_ele).isdigit():
    print(search_ele, " is Numeric")
else:
    print(search_ele, " is a string")

if flag != 0:
    print("YES! {} exists in the list".format(search_ele))
else:
    print("YES! {} doesn't exist in the list".format(search_ele))