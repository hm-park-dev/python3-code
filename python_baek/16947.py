# 16947.py 서울 지하철 2호선
# https://www.acmicpc.net/problem/16947

# n번 역과 순환선 사이의 거리를 출력
# 사이클을 찾아야함?

import sys
input = sys.stdin.readline

def dfs(target):
    visited[target] = True

    for node in graph[target]:
        if not visited[node]:
            dfs(node)

# Initial
answer = list()
N = int(input())
graph = [[] for _ in range(N + 1)] # 1 ~ N node

for _ in range(N):
    a, b = map(int, input().split())
    # Undirected Graph
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(N+1)]
# 1. Find the Cycle


# Answer
print(' '.join(map(str, answer)))