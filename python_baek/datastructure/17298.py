# 17298.py 오큰수
import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
ans = [-1 for _ in range(N)]
# 인덱스를 저장하는 스택
stack = list()

stack.append(0)

for i in range(1, N):
    # 스택이 끝날 때 까지 오큰수를 찾아본다
    while stack and A[stack[-1]] < A[i]:
        ans[stack.pop()] = A[i]
    stack.append(i)

print(' '.join(map(str, ans)))