def remove_duplicate(arr):
    unique_list = []
    for ele in arr:
        if ele not in unique_list:
            unique_list.append(ele)
    return unique_list

arr = [1, 3, 5, 1, 3, 7, 9]
print(remove_duplicate(arr))