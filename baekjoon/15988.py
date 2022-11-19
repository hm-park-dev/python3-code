# 15988.py 1, 2, 3 더하기 3
# https://www.acmicpc.net/problem/15988

import sys
input = sys.stdin.readline

# Initial
answer = list()
mod = 1000000009
MAX = 1000000

# Make DP table
dp = [0 for _ in range(MAX + 1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, MAX + 1):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % mod

# Answer
for _ in range(int(input())):
    n = int(input())
    answer.append(dp[n])

print('\n'.join(map(str, answer)))