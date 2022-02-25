# 17299.py 오등큰수

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))

stack = list()
ans = [-1 for _ in range(N)]
f = [0 for _ in range(1000001)]

stack.append(0)

for i in range(N):
    # f를 증가
    f[A[i]] += 1

# 오큰수와 같은 방식으로 품
# 스택이 끝날 때 까지 오등큰수를 찾아본다
for i in range(1, N):
    while stack and f[A[stack[-1]]] < f[A[i]]:
        ans[stack.pop()] = A[i]
    stack.append(i)

print(' '.join(map(str, ans)))