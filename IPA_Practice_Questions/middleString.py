def middleString(t, N):
    #pass
    middle=int(len(t)//2)
    if len(t) % 2 != 0:
        x=t[middle:middle+N]
    else:
        x=t[middle-1:middle+N-1]
    if len(x) == 0:
        return t[-1]
    else:
        return x


t=input()
N=int(input())
print(middleString(t, N))