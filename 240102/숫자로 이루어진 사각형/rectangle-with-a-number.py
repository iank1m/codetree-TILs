n = int(input())
k = 1

def forn(n,t):
    for i in range(n):
        print("%d"%t,end=' ')
        t += 1
        if t > 9:
            t = 1
    print(" ")
    return t

for i in range(n):
    k = forn(n,k)
    if k>9:
        k=1