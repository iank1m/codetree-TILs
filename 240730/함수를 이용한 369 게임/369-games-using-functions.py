a, b = map(int, input().split())

def count_369(a, b):
    cnt = 0
    for i in range(a, b + 1):
        k = 1
        while k <= i:
            if (i // k) % 10 in {3, 6, 9}:
                cnt += 1
                break  # 3, 6, 9를 포함하면 더 이상 확인할 필요 없음
            k *= 10
        else:
            if i % 3 == 0:
                cnt += 1
    return cnt

print(count_369(a, b))