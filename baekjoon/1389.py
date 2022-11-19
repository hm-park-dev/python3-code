# 1389.py 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

import sys
input = sys.stdin.readline

# Initial
N, M = map(int, input().split())
user = [[] for _ in range(N + 1)]
kevin = [N for _ in range(N+1)] # Save Kevin number
answer = 0

# Make Undirected Graph
for _ in range(M):
    a, b = map(int, input().split())
    if b in user[a]: # duplicated relation
        continue
    else:
        user[a].append(b)
        user[b].append(a)

# Answer
print(answer)