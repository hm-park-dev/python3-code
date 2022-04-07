# 1912.py 연속합
# https://www.acmicpc.net/problem/1912

import sys
input = sys.stdin.readline

# Initial
answer = 0
n = int(input())
arr = list(map(int, input().split()))

# Make dp table
dp = [0 for _ in range(n)]
dp[0] = arr[0]
for i in range(1, n):
    if arr[i] <= arr[i] + dp[i-1]:
        dp[i] = arr[i] + dp[i-1]
    else:
        dp[i] = arr[i]
    # print(f"[DEBUG] i: {i}, arr[{i}]: {arr[i]}, dp[{i}]: {dp[i]}")

# Answer
answer = max(dp)
print(answer)