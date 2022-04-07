# 2577.py 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

num = list(map(int, str(A * B * C)))
ret = [0 for _ in range(10)]

for i in range(len(num)):
    ret[num[i]] += 1

for i in range(10):
    print(ret[i])