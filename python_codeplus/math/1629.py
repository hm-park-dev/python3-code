# 1629.py 곱셈

# 10^11 -> 10^(1011) 이진수의 원리를 사용
def pow_custom(a: int, b: int, c: int) -> int:
    ret = 1
    
    while b:
        if b % 2 == 1:
            ret = ret * a % c
        a = a * a % c
        b //= 2
    return ret

a, b, c = map(int, input().split())
print(pow_custom(a, b, c))