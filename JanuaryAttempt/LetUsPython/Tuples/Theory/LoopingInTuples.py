# while and for loop
tpl = (10, 20, 30, 40, 50)
i = 0
while i < len(tpl):
    print(tpl[i])
    i += 1
for n in tpl:
    print(n)


# enumerate
for index, n in enumerate(tpl):
    print(index, n)