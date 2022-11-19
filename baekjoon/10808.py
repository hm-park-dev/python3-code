# 10808.py 알파벳 개수
# https://www.acmicpc.net/problem/10808

S = list(input())
alpha = [0 for _ in range(26)]

for s in S:
    alpha[ord(s) - ord('a')] += 1

print(' '.join(list(map(str, alpha))))