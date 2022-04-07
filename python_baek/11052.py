# 11052.py 카드 구매하기
# https://www.acmicpc.net/problem/11052

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
    temp = 0
    for j in range(1, i):
        temp = max(temp, dp[i-j] + P[j])
    dp[i] = max(temp, P[i])

# Answer
answer = dp[N]
print(answer)