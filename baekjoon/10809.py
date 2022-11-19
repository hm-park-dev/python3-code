# 10809.py 알파벳 찾기
# https://www.acmicpc.net/problem/10809

S = list(input())
alpha = [-1 for _ in range(26)]

for i in range(len(S)):
    if alpha[ord(S[i]) - ord('a')] == -1:
        alpha[ord(S[i]) - ord('a')] = i

print(' '.join(list(map(str, alpha))))