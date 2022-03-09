# 11656.py 접미사 배열
# https://www.acmicpc.net/problem/11656

S = input()
suffix = []

for i in range(len(S)):
    suffix.append(S[i:])

suffix.sort()
print('\n'.join(suffix))