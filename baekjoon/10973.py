# 10973.py 이전 순열
# https://www.acmicpc.net/problem/10973

# 이전에 나온 순열을 구하는 문제

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if arr[i-1] > arr[i]: # 앞 열의 값이 그 뒷열의 값보다 크다면
        for j in range(N-1, 0, -1):
            if arr[i-1] > arr[j]: # 그 앞의 열 값이 뒤에 있는 값보다 크다면
                arr[i-1], arr[j] = arr[j], arr[i-1] # 그 두 값을 스왑함
                arr = arr[:i] + sorted(arr[i:], reverse=True)
                print(*arr)
                exit()
print(-1)