# 1699.py 제곱수의 합
# https://www.acmicpc.net/problem/1699

# 항의 최소 개수를 구함

import sys
input = sys.stdin.readline

# Initial
N = int(input())
MAX = 100000
answer = 0

# Make dp table
dp = [0 for _ in range(MAX + 1)]
dp[1] = 1 # 1 = 1^2

for i in range(2, MAX + 1):
    dp[i] = i
    for j in range(1, i):
        if (j**2) > i:
            break
        if dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1
            
# Answer
answer = dp[N]
print(answer)