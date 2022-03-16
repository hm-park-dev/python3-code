# 11726.py 2×n 타일링
# https://www.acmicpc.net/problem/11726

n = int(input())
dp = [0 for _ in range(1001)]
answer = 0

# 세로로 한 번
dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = dp[i-2] + dp[i-1]

answer = dp[n]
print(answer % 10007)