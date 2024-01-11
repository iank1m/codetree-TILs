def calculate_sum(n):
    # 기저 조건: n이 100 이상이면 0을 반환
    if n >= 100:
        return 0

    # 현재 숫자가 짝수이면 짝수의 합을 구하는 경우
    if n % 2 == 0:
        return n + calculate_sum(n + 2)

    # 현재 숫자가 홀수이면 홀수의 합을 구하는 경우
    else:
        return n + calculate_sum(n + 2)

def main():
    n = int(input("정수 n을 입력하세요: "))
    result_sum = calculate_sum(n)
    print(result_sum)

if __name__ == "__main__":
    main()