# 1018.py 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

import sys
input = sys.stdin.readline

# Initial
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
answer = []

for i in range(N-7):
    for j in range(M-7):
        first_w = 0
        first_b = 0
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if MAP[a][b] != 'W':
                        first_w += 1
                    if MAP[a][b] != 'B':
                        first_b += 1
                else:
                    if MAP[a][b] != 'B':
                        first_w += 1
                    if MAP[a][b] != 'W':
                        first_b += 1
        
        answer.append(min(first_w, first_b))

# Answer
print(min(answer))