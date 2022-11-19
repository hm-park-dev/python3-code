# 11053.py 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

# 가장 긴 부분 수열의 길이를 구하는 프로그램

# Initial
N = int(input())
A = list(map(int, input().split()))
answer = 0

# Make dp table
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# Answer
answer = max(dp)
print(answer)