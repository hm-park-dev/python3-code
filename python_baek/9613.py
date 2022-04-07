# 9613.py GCD 합
# https://www.acmicpc.net/problem/9613
import sys 

def gcd(a: int, b: int):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for _ in range(int(input())):
    n, *nums = map(int, sys.stdin.readline().split())
    sum_gcd = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            a, b = nums[i], nums[j]
            sum_gcd = sum_gcd + gcd(a, b)
    
    print(sum_gcd)