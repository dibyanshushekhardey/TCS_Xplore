lst = [10, 2, 0, 50, 4]
lst.reverse()
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

print(sorted(lst))
print(sorted(lst, reverse=True))
print(list(reversed(lst)))

print(lst[::-1])