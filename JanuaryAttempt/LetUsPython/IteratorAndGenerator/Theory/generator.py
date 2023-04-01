def avgAdj(data):
    for i in range(0, len(data)-1):
        yield (data[i]+data[i+1])/2

lst=[10, 20, 30, 40, 50, 60, 70]
for i in avgAdj(lst):
    print(i)