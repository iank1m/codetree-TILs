a,b=map(int,input().split())

arr = []
for i in range(a,b+1):
    arr.append(i)
    
def count_369(arr):
    cnt = 0
    k=1
    i=0
    while k<10*len(arr) and i<len(arr):
        if arr[i]%k==3 or arr[i]%k==6 or arr[i]%k==9:
            cnt +=1
        elif arr[i]%3 == 0:
            cnt += 1
        i += 1
        k = k*10
    return cnt

print(count_369(arr))