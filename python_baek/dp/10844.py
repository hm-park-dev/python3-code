# 10844.py 쉬운 계단 수
# https://www.acmicpc.net/problem/10844

# Initial
N = int(input())
dp = [0 for _ in range(N+1)]
answer = 0
mod = 1000000000

# Make DP table
dp[1] = 9


# Answer
answer = dp[N]
print(answer)