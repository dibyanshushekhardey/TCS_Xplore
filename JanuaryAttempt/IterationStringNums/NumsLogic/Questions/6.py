# WAP to read numbers form a single line and print the missing numbers
# numbers will be in consecutive order

n = list(map(int, input().split()))
n0 = min(n)
n1 = max(n)
l = [x for x in range(n0, n1+1)]

for i in l:
    if i not in n:
        print(i, end=" ")
