try:
    lst=[10, 20, 30, 40, 50]
    for num in lst:
        i=int(num)
        j=i*i
        print(i, j)
except NameError:
    print(NameError.args)
else:
    print('Total numbers processed {}'.format(len(lst)))
    del(lst)