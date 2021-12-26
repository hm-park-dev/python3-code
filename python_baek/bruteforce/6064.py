# 6064.py 카잉 달력

def solution(M, N, x, y):
    year = 1
    a, b = 1, 1
    while True:
        if a > M:    a = 1
        if b > N:    b = 1

        # 맞을 때
        if a == x and b == y:
            print(year)
            break
        # 끝날 때
        if a == M and b == N:
            print(-1)
            break
        
        year += 1
        a += 1
        b += 1

T = int(input())
for _ in range(T): 
    M, N, x, y = map(int, input().split())
    solution(M, N , x, y)