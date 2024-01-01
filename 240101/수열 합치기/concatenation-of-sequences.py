size = list(map(int, input().split())) #필요없는데
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.extend(b)
a.sort()

for i in range (len(a)):
    print(a[i], end=" ")