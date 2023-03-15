'''
Though map( ) function is available ready-made in Python, can you
define one yourself and test it?
'''

def my_map(fun, seq):
    result=[]
    for ele in seq:
        result.append(fun(ele))
    return result

lst1=[5, 7, 9, -3, 4, 2, 6]
lst2=list(my_map(lambda n:n**2, lst1))
print(lst2)