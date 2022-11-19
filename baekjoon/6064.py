# 6064.py 카잉 달력

def solution(M, N, x, y):
    # (year - x) % M = 0
    # (year - y) % N = 0
    # 되는것을 찾아야함
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1

T = int(input())
for _ in range(T): 
    M, N, x, y = map(int, input().split())
    print(solution(M, N , x, y))