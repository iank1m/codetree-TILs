targets = input()
x, y = 0,0 #현재위치
dir_num = 3 #북쪽을 바라보고 시작

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for target in targets:
    if target == "L":#반시계로 90도
        dir_num = (dir_num + 3)%4
    elif target == "R": #시계방향으로 90도
        dir_num = (dir_num +1)%4
    else:
        #F인경우 / 바라보고있는 방향으로 한칸 앞으로
        x,y = x+dx[dir_num], y+dy[dir_num]

print(x,y)