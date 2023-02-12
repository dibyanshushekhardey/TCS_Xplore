ls = []
ls.append(10)
ls.extend([11, 12, 13])
ls.insert(1, 22)
print("Insertion results", ls, sep="\n")

# pop, pop(n), remove()
deleted_last=ls.pop() # returns the deleted list
print("ls.pop()", ls, sep=" => ")
deleted = ls.pop(1) #deletes an element from index 1
print("ls.pop(1)", ls, sep=" => ")
ls.remove(11) #deleted the specified element do not return element
print("ls.remove(11)", ls, sep=" => ")
