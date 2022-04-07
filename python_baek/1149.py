# 1149.py RGB 거리
# https://www.acmicpc.net/problem/1149
# 모든 인접한 집의 색은 일치하지 않는다.
import sys
input = sys.stdin.readline

# Initial
answer = 0 # 모든 집을 칠하는 비용의 최솟값
N = int(input())
houses = [[0 for _ in range(3)] for _ in range(N)]
for i in range(N):
    houses[i] = list(map(int, input().split()))

# Answer
print(answer)