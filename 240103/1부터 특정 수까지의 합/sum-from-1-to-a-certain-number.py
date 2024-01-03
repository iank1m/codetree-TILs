n=int(input())

def test(n,k):
    for i in range(1,n+1,1):
        k += i
    return k

result = round(test(n,1)/10)
print(result)