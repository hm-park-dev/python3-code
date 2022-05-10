# 7576.py 토마토
# https://www.acmicpc.net/problem/7576

# 1 익은 토마토
# 0 익지 않은 토마토
# -1 토마토가 들어있지 않은 칸

import sys
from collections import deque
input = sys.stdin.readline

# Initial
M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

answer = 0 # 최소날짜, 이미 모든 토마토가 익었다면 0, 모두 익지는 못 한다면 -1 

# 익은 토마토의 위치 찾기
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            queue.append([i, j, 0])

# BFS
while queue:
    v = queue.popleft()
    i, j, cnt = v[0], v[1], v[2]
    answer = cnt

    # [i-1, j]
    if 0 <= i-1 < N:
        if MAP[i-1][j] == 0:
            MAP[i-1][j] = 1
            queue.append([i-1, j, cnt+1])
    # [i+1, j]
    if 0 <= i+1 < N:
        if MAP[i+1][j] == 0:
            MAP[i+1][j] = 1
            queue.append([i+1, j, cnt+1])
    # [i, j-1]
    if 0 <= j-1 < M:
        if MAP[i][j-1] == 0:
            MAP[i][j-1] = 1
            queue.append([i, j-1, cnt+1])
    # [i, j+1]
    if 0 <= j+1 < M:
        if MAP[i][j+1] == 0:
            MAP[i][j+1] = 1
            queue.append([i, j+1, cnt+1])  

# 모두 익었는지 확인
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0:
            answer = -1
            break

print(answer)