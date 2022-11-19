# 1672.py DNA 해독
# https://www.acmicpc.net/problem/1672
# pypy3 -> 메모리 초과가 나오는 경우가 있음, 그럴경우 python3로 언어 변경해서 제출

N = int(input())
s = list(input())

dna = {
    'A': {'A': 'A', 'G': 'C', 'C': 'A', 'T': 'G'},
    'G': {'A': 'C', 'G': 'G', 'C': 'T', 'T': 'A'},
    'C': {'A': 'A', 'G': 'T', 'C': 'C', 'T': 'G'},
    'T': {'A': 'G', 'G': 'A', 'C': 'G', 'T': 'T'}
}
for _ in range(N-1):
    row = s.pop()
    col = s.pop()
    chr = dna[row][col]
    s.append(chr)

print(s[0])