# 1934.py 최소공배수
# https://www.acmicpc.net/problem/1934

import sys

def get_gcd(a: int, b: int) -> int:
    if a < b:
        return get_gcd(b, a)
    if b == 0:
        return a
    else:
        return get_gcd(b, a%b)

def solution(a: int, b: int):
    return print(int(a * b / get_gcd(a, b)))

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    solution(a, b)