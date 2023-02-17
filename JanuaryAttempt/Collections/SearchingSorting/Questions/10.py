my_dict = {'beth':37, 'zane':32, 'john':41, 'amy':41, 'mike':59, 'jane':43}
sorted_dict = dict(sorted(my_dict.items()))
print('sorted dictionary: ', sorted_dict)

sorted_dict_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print('sorted dict by value: ', sorted_dict_value)