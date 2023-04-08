str1=input()
str2=input().lower()
flag=False

for word in str1.split():
    for ch in word:
        if not ch.lower() in str2:
            flag =True
            break
    if flag:
        break

if flag:
    print('Input string is not valid')
    print(str1)
else:
    print('Input string is valid')
    print(str1)