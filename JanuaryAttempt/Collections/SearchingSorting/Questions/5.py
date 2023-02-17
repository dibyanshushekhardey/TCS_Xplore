def count_dig(tup):
    return sum([len(str(ele)) for ele in tup ])

list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
list.sort(key = count_dig)
print(list)