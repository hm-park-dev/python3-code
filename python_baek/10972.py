# 10972.py 다음 순열
# https://www.acmicpc.net/problem/10972

# 사전순으로 다음에 오는 순열을 구하는 프로그램
from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
arr = tuple(map(int, input().split()))
items = [i for i in range(1, N+1)]

permu = list(permutations(items, N))
index = permu.index(arr)
if index == len(permu) - 1:
    print(-1)
else:
    print(' '.join(map(str,permu[index+1])))