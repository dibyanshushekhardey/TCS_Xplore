
def helper(n, t, lol):
    global j
    if len(t) == n:
        #lol[j] = lol[j] + t
        #j += 1
        return
    for i in range(1, n+1):
        t.append(i)
        helper(n, t, lol)
        t.pop()

def generate(n):
    t=[]
    lol=[[] for i in range(n**n)]
    helper(n, t, lol)
    return lol


j=0
l=generate(3)
print(l)