# use of list comprehension
data = input()
frequencies = [data.count(i) for i in data]
print(max(frequencies))