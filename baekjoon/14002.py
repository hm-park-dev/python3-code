# 14002.py 가장 긴 증가하는 부분 수열4
# https://www.acmicpc.net/problem/14002

# 가장 긴 증가하는 부분 수열의 길이
# 그런 수열을 출력

# Initial
N = int(input())
A = list(map(int, input().split()))
answer_arr = []
answer_len = 0

# Make dp table
# 이어지는 이전 값의 인덱스를 저장??
# 마치 Linked List처럼!
dp = [1 for _ in range(N)]
pre_index_table = [i for i in range(N)]
for i in range(N):
    arr = list()
    for j in range(i):
        if A[i] > A[j]:
            # dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > dp[j] + 1:
                dp[i] = dp[i]
            elif dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                pre_index_table[i] = j

answer_len = max(dp)
target = dp.index(answer_len)
# 이전 인덱스 탐색
for _ in range(answer_len):
    # print("[DEBUG] now target:", target)
    answer_arr.insert(0, A[target])
    target = pre_index_table[target]

# Answer
print(answer_len)
print(' '.join(map(str, answer_arr)))