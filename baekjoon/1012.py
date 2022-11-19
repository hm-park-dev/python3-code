# 1012.py
# https://www.acmicpc.net/problem/1012

from collections import deque
import sys
input = sys.stdin.readline

# BFS
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, i, j):
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0 # visited

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


# Initial
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    baechu = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        baechu[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if baechu[i][j] == 1:
                bfs(baechu, i, j)
                answer += 1

    # Answer
    print(answer)