# 16194.py 카드 구매하기2
# https://www.acmicpc.net/problem/16194

# Initial
N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)
dp = [0 for _ in range(N+1)]
answer = 0

# P[n] = 카드 n개가 포함된 카드팩의 가격

# Make DP table
dp[1] = P[1]
for i in range(1, N+1):
    temp = float("inf")
    for j in range(1, i):
        temp = min(temp, dp[i-j] + P[j])
    dp[i] = min(temp, P[i])

# Answer
answer = dp[N]
print(answer)