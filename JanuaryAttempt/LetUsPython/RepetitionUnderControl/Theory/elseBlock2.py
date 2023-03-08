for ele in [10, 20, 30, 3, 40, 50]:
    if ele % 10 != 0:
        print(ele, 'is not a multiple of 10')
        break
else:
    print('all numbers in list are multiples of 10')