def to_decimal(n, base):
    decimal_value = 0
    power = 0
    while n > 0:
        digit = n % 10
        decimal_value += digit * (base ** power)
        n //= 10
        power += 1
    return decimal_value

def to_base_b(n, base):
    if n == 0:
        return '0'
    
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    converted = ''
    while n > 0:
        digit = n % base
        converted = digits[digit] + converted
        n //= base
    return converted

def base_converter(N, A, B):
    # A진법의 숫자를 10진수로 변환
    decimal_number = to_decimal(N, A)
    
    # 10진수를 B진법으로 변환
    result = to_base_b(decimal_number, B)
    
    return result

# 입력값 받기
A, N, B = input().split()
N = int(N)
A = int(A)
B = int(B)

# 변환 결과 출력
result = base_converter(N, A, B)
print(result)