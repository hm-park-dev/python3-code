# 1149.py RGB 거리
# https://www.acmicpc.net/problem/1149
# 모든 인접한 집의 색은 일치하지 않는다.
import sys
input = sys.stdin.readline

# Initial
answer = 0 # 모든 집을 칠하는 비용의 최솟값
N = int(input())
houses = [[0 for _ in range(3)] for _ in range(N)] # 빨강, 초록, 파랑
for i in range(N):
    houses[i] = list(map(int, input().split()))

# Make dp table
# dp[i][0] = i번째 에서 빨강을 사용할 때 비용
# dp[i][1] = i번째 에서 초록을 사용할 때 비용
# dp[i][2] = i번째 에서 파랑을 사용할 때 비용
dp = [[0 for _ in range(3)] for _ in range(N)]
for i in range(N):
    if i == 0:
        dp[i][0] = houses[i][0]
        dp[i][1] = houses[i][1]
        dp[i][2] = houses[i][2]
    else:
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i][2]


# Answer
answer = min(dp[N - 1])
print(answer)