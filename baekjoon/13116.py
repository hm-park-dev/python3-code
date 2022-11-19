# 13116.py 30번
# 이진 트리에서 제일 가까운 공통 조상 찾기

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    while A != B:
        if A > B: A //= 2
        else: B //= 2

    print(A * 10)
