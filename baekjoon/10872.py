# 10872.py 팩토리얼
# https://www.acmicpc.net/problem/10872

def get_factorial(N: int) -> int:
    if N == 0:
        return 1
    else:
        return N * get_factorial(N-1)

N = int(input())
print(get_factorial(N))