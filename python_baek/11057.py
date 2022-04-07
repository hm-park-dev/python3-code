# 11057.py 오르막 수
# https://www.acmicpc.net/problem/11057

# 수의 자리가 오름차순을 이르는 수
# 인접한 수가 같아도 오름차순으로 침
# 수의 길이 N개가 주어졌을 때, 오르막 수의 개수를 구하는 프로그램
# 수는 0으로 시작할 수 있다.

import sys
input = sys.stdin.readline

# Initial
answer = 0
mod = 10007
N = int(input())

# Answer 
print(answer % mod)