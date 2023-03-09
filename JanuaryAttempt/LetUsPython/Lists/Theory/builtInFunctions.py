lst1 = [10, 20, 30, 40, 50]
#lst=del(lst[3])
del(lst1[2:5])
lst=[]
print(lst)

lst1 = [10, 20, 30, 40, 50]
lst3 = lst2 = lst1
lst1 = []
print(lst2)

lst2[:] = []
print(lst2)
print(lst3)
