# 15664.py N과 M (10)
# https://www.acmicpc.net/problem/15664

# N개의 자연수(nums) 중에서 길이가 M인 수열
# 고른 수열은 비내림차순
# A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK
# 중복된 수열은 여러 번 출력하지 않는다.

import sys
import copy
input = sys.stdin.readline

# Initial
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
stack = list()
visited = list()

def solution(stack, idx):
    # print('[DEBUG] stack:', stack)
    if len(stack) == M:
        if stack not in visited:
            # Answer
            print(' '.join(map(str, stack)))
            visited.append(copy.deepcopy(stack))
            
        return

    for i in range(idx+1, N):
        if nums[i] >= stack[-1]: 
            stack.append(nums[i])
            solution(stack, i)
            stack.pop()


for i in range(N):
    stack.append(nums[i])
    # print('[DEBUG] start with', nums[i])
    solution(stack, i)
    stack.pop()