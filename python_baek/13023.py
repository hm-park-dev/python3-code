# 13023.py ABCDE
# https://www.acmicpc.net/problem/13023

import sys
input = sys.stdin.readline

# Initial
answer = 0
N, M = map(int, input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    # Undirected Graph
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Answer
print(answer)