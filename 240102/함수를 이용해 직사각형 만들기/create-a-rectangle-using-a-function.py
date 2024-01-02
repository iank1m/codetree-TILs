n,m=tuple(map(int,input().split()))

def form(m):
    for i in range (0,m):
        print('1',end='')
    print(" ")
    #이거 때문에 한참 고민함... end='' 때문에 원하는 줄바꿈이 안될 땐 \n말고 공백출력으로 해결하기..

for i in range(0,n):
    form(m)