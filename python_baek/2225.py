# 2225.py 합분해
# https://www.acmicpc.net/problem/2225

import sys
input = sys.stdin.readline

# Initial
N, K = map(int, input().split())
mod = 1000000000
answer = 0

# Make DP Table
# 0 을 조합해 무조건 N번째 수는 K개 이상이 나올 수 있음
dp = [[k for _ in range(N+1)] for k in range(K+1)]

for k in range(2, K + 1):
    for i in range(2, N+1):
        dp[k][i] = (dp[k-1][i] + dp[k][i-1]) % mod

# Answer
answer = dp[K][N]
print(answer % mod)