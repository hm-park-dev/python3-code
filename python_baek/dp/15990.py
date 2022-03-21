# 15990.py 1, 2, 3 더하기 5
# https://www.acmicpc.net/problem/15990

import sys

# Initial
# n의 최댓값
MAX = 100000
mod = 1000000009

# Make DP table
dp = [[0 for _ in range(4)] for _ in range(MAX + 1)]
# nth -> i / 마지막에 사용한 수 j
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, MAX + 1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % mod
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % mod
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % mod

# Input n value
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    # Answer
    answer = sum(dp[n]) % mod
    print(answer)