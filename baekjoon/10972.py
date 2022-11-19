# 10972.py 다음 순열
# https://www.acmicpc.net/problem/10972

# 사전순으로 다음에 오는 순열을 구하는 프로그램

# permutations 사용시 메모리초과 등등

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if arr[i-1] < arr[i]:   # 앞 열의 값이 그 뒷열의 값보다 작으면
        for j in range(N-1, 0, -1): # 그 앞 열의 값을 맨 뒷열부터 비교
            if arr[i-1] < arr[j]:   # 그 앞 열의 값이 뒤에 있는 열보다 작을경우
                arr[i-1], arr[j] = arr[j], arr[i-1] # 그 두 값을 스왑함
                arr = arr[:i] + sorted(arr[i:])
                print(*arr)
                exit()

print(-1)