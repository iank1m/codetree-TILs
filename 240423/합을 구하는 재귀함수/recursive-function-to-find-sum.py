def sum(n):
    s = 0
    while(n<=100):
        s += n
        n += 2
    return s

n = int(input())
if (n<=100):
    print(sum(n))
else:
    exit(1)