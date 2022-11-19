# 1074.py Z
# https://www.acmicpc.net/problem/1074

import sys
input = sys.stdin.readline

# Initial
N, r, c = map(int, input().split())
answer = 0

# Divide and Conqure
while N != 0:
    N -= 1

    if r < 2 ** N and c < 2 ** N: # Quadrant 1
        answer += (2 ** N) * (2 ** N) * 0
    elif r < 2 ** N and c >= 2 ** N: # Quadrant 2
        answer += (2 ** N) * (2 ** N) * 1
        c -= 2 ** N
    elif r >= 2 ** N and c < 2 ** N: # Quadrant 3
        answer += (2 ** N) * (2 ** N) * 2
        r -= 2 ** N
    else: # Quadrant 4
        answer += (2 ** N) * (2 ** N) * 3
        c -= 2 ** N
        r -= 2 ** N

# Answer
print(answer)