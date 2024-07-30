n = int(input()) # 총 몇 번 움직일건지

x,y=0,0 #현재위치
dx,dy = [1,0,-1,0],[0,-1,0,1]

for _ in range(n):
    # W : Way방향 / D : Distance 거리
    W, D = map(str, input().split())
    D = int(D) #D를 숫자로 바꿔두고
    
    if W == 'E':
        direction = 0
    elif W == 'S':
        direction = 1
    elif W == 'W':
        direction = 2
    else: # N
        direction = 3

    x += dx[direction] * D
    y += dy[direction] * D

print(x,y)