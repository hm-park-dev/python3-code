# 1260.py DFS와 BFS
# https://www.acmicpc.net/problem/1260

# 방문할 수 있는 점이 없는 경우 종료

import sys
from collections import deque
input = sys.stdin.readline

# DFS
def dfs(start):
    print(start, end=' ')
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            dfs(node)

    return

# BFS
def bfs(start):
    visited[start] = True
    queue = deque()
    queue.append(start)

    while queue:
        target = queue.popleft()
        print(target, end=' ')

        for node in graph[target]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True

    return

# Initial
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    # 양방향 그래프
    graph[a].append(b)
    graph[b].append(a)

# sort
for i in range(1, N+1):
    graph[i].sort()

# Answer
visited = [False for _ in range(N+1)]
dfs(V)

print()

visited = [False for _ in range(N+1)]
bfs(V)