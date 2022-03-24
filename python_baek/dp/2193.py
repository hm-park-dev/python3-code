# 2193.py 이친수
# https://www.acmicpc.net/problem/2193

# 이진수 중 0으로 시작되지 않음
# 1이 두 번 연속으로 나타나지 않음

# Initial
N = int(input()) # 1 <= N <= 90
dp = [[0 for _ in range(2)] for _ in range(91)]
answer = 0

# Make DP table
dp[1][0] = 0
dp[1][1] = 1

for i in range(2, 91):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

# Answer
answer = sum(dp[N])
print(answer)