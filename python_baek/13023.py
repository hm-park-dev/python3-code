# 13023.py ABCDE
# https://www.acmicpc.net/problem/13023

# 연속된 4개의 수가 나와야함?
# 최소 탐색 길이가 4일때 나오기?

import sys
input = sys.stdin.readline

# DFS
def dfs(target, num):
    if num == 4:
        print(1)
        exit()

    for node in graph[target]:
        if not visited[node]:
            visited[node] = True
            dfs(node, num + 1)
            visited[node] = False


# Initial
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    # Undirected Graph
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False for _ in range(N)]

for node in range(N):
    visited[node] = True
    dfs(node, 0)
    visited[node] = False

print(0)