# 방향에 따른 이동 좌표 변화
direction_mapper = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

# 입력 처리
N = int(input())
movements = [input().split() for _ in range(N)]
movements = [(d, int(dist)) for d, dist in movements]

# 초기 위치와 시간 초기화
x, y = 0, 0
time = 0

# 이동 처리
for d, dist in movements:
    dx, dy = direction_mapper[d]
    for _ in range(dist):
        x += dx
        y += dy
        time += 1
        if x == 0 and y == 0:
            print(time)
            exit()

# 만약 (0, 0)으로 돌아오지 않았다면 -1 출력
print(-1)