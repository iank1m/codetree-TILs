N=int(input())

def go(n):
    target = 0
    for i in range(1,n+1):
        target += i
    return target//10

print(go(N))