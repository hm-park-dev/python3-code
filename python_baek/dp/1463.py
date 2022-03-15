# 1463.py  1로 만들기
# https://www.acmicpc.net/problem/1463

N = int(input())
dp = [0 for _ in range(10**6 + 1)]
answer = 0

dp[2] = 1
dp[3] = 1

for i in range(4, len(dp)):
    dp[i] = 1 + dp[i-1]
    if i % 2 == 0:
        dp[i] = min(dp[i], 1 + dp[i//2])
    if i % 3 == 0:
        dp[i] = min(dp[i], 1 + dp[i//3])

answer = dp[N]
print(answer)