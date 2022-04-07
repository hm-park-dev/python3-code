# 1309.py 동물원
# https://www.acmicpc.net/problem/1309

# 가로로도 세로로도 붙어 있게 배치할 수 없음
# 2 * N 배열에 사자를 배치하는 경우의 수
# 사자를 한 마리라도 배치하지 않는 경우도 하나의 경우의 수
# 사자의 수는 정해지지 않았다.

import sys
input = sys.stdin.readline

# Initial
answer = 0
mod = 9901
N = int(input())

# Make dp Table
# dp[i][0]: i 번째 줄에 사자 없을 때 경우의 수 
# dp[i][1]: i 번째 줄에 사자 있을 때 경우의 수
dp = [[0 for _ in range(2)] for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 2
for i in range(1, N):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % mod
    dp[i][1] = (dp[i-1][0] * 2 + dp[i-1][1]) % mod

# Answer
answer = sum(dp[N-1])
print(answer % mod)