def find_return_time(commands):
    # 방향 인덱스: 0 = N, 1 = E, 2 = S, 3 = W
    direction_index = 0
    
    # 방향에 따른 dx, dy 변화량 설정
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W 순서
    x, y = 0, 0  # 초기 위치
    time_elapsed = 0  # 경과 시간
    
    for command in commands:
        # 명령에 따라 시간 및 위치 변경
        if command == 'L':
            direction_index = (direction_index - 1) % 4
            time_elapsed += 1
        elif command == 'R':
            direction_index = (direction_index + 1) % 4
            time_elapsed += 1
        elif command == 'F':
            dx, dy = directions[direction_index]
            x += dx
            y += dy
            time_elapsed += 1
        
        # (0, 0)으로 돌아왔는지 확인
        if x == 0 and y == 0:
            return time_elapsed
    
    # 끝까지 돌아오지 못했다면 -1 출력
    return -1

# 예제 실행
commands = input().strip()
result = find_return_time(commands)
print(result)