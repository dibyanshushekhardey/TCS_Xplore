def countString(arr):
    count = 0
    for ele in arr:
        if len(ele) >= 2 and (ele[0] == ele[-1]):
            count += 1
    return count

arr = ['abc', 'xyz', 'aba', '1221']
print(countString(arr))