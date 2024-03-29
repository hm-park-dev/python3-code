# 10844.py 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

# Initial
N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)]
answer = 0
mod = 1000000000

# Make DP table
for i in range(1, 10):
    dp[1][i] = 1
if N > 1: 
    for i in range(2, N+1):
        for j in range(0, 10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1] % mod
            elif j == 9:
                dp[i][j] = dp[i-1][j-1] % mod
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
        

# Answer
for i in range(10):
    answer = (answer + dp[N][i]) % mod
print(answer)