a,b,c = map(int, input().split())

def cal(a,b,c):

    arr = [a,b,c]
    arr = sorted(arr)
    return arr[0]

print(cal(a,b,c))