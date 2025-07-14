n = int(input())
num = 1

for _ in range(n):
    for _ in range(n):
        print(num, end=' ')
        num += 1
        if num == 10:  # 10이 되면 다시 1로 초기화
            num = 1
    print()
