# 2588.py 곱셈

a = int(input())
b = int(input())

b1 = b % 10
b2 = b % 100 - b1
b3 = b - b2 - b1

ret1 = a * b1
ret2 = a * b2
ret3 = a * b3

print(ret1)
print(int(ret2 / 10))
print(int(ret3 / 100))
print(ret1 + ret2 + ret3)