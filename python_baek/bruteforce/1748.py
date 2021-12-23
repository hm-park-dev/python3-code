# 1748.py 수 이어쓰기1

N = int(input())
ret = 0
a = len(str(N)) - 1

for i in range(a):
    ret += 9 * (10 ** i) * (i + 1)
    i += 1
ret += (N - (10 ** a) + 1) * (a + 1)

print(ret)