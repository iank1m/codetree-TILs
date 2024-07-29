n = int(input())

def cal(n):
    first = n//10
    second = n%10
    make = first + second
    if n%2==0 and make%5==0:
        return 1
    else:
        return 0

if cal(n) is 1:
    print("Yes")
else:
    print("No")