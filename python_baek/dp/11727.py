# 11727.py 2×n 타일링 2
# https://www.acmicpc.net/problem/11727

n = int(input())
dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = 2 * dp[i-2] + dp[i-1]

print(dp[n] % 10007)