n,t = map(int,input().split())

#r,c,d = map(int,input().split())
r,c,d = input().split()

#방향설정해주고
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

#딕셔너리 만들어놔
mapper = {
    'U': 2, #up
    'D': 1, #down
    'R': 0, #right
    'L': 3 #left
}

#in_range
def in_range(x,y):
    return 0<=x and 0<=y and x<n and y<n

#x,y를 0에 대한 좌표로 해야하니까
x = int(r)-1
y = int(c)-1
#방향도 (문자주의)
direction = mapper[d]

#구슬 굴려!!
for _ in range(t):
    nx,ny = x+dxs[direction], y+dys[direction]

    if in_range(nx,ny): #범위 안에 있는거면
        x=nx
        y=ny #그대로 이동
    else: #경계에 닿았다면
        direction = 3-direction #방향전환

print(x+1,y+1)