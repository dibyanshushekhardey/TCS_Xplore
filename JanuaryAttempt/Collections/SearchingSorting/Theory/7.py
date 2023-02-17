def combine_dict(dict1, dict2):
    combined_dict = {}
    for key in dict1:
        combined_dict[key] = dict1[key]
    for key in dict2:
        if key in combined_dict:
            combined_dict[key] += dict2[key]
        else:
            combined_dict[key] = dict2[key]
    return combined_dict

d1 = {'a':100, 'b':200, 'c':300}
d2 = {'a':300, 'b':200, 'd':400}
print(combine_dict(d1, d2))