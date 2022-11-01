# 1181.py 단어 정렬
# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

N = int(input())
alpha = list()

for _ in range(N):
    a = input()
    if a not in alpha:
        alpha.append(a)

new_list = sorted(alpha, key=lambda x: (len(x), x))
print(''.join(new_list))