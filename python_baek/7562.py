# 7562.py
# https://www.acmicpc.net/problem/7562

# 필요없는 방향은 제거

import sys
from collections import deque
input = sys.stdin.readline

knights = [[-2, 1], [-1, 2], [1, 2], [2, 1],
            [-2, -1], [-1, -2], [1, -2], [2, -1]]

def solution(l, start_x, start_y, target_x, target_y):
    MAP = [[False for _ in range(l)] for _ in range(l)] # visited table
    MAP[start_x][start_y] = True
    queue = deque()
    answer = 0
    ret = deque()
    ret.append(answer)

    if start_x == target_x and start_y == target_y:
        return answer

    # 처음 위치 넣기
    cnt = ret.popleft()
    for move in knights:
        temp_x = start_x + move[0]
        temp_y = start_y + move[1]

        if 0 <= temp_x < l and 0 <= temp_y < l and not MAP[temp_x][temp_y]:
            queue.append([temp_x, temp_y])
            MAP[temp_x][temp_y] = True
            ret.append(cnt+1)

    answer = 1
    while(queue):
        node = queue.popleft()
        cnt = ret.popleft()

        # print(f'[DEBUG] now x: {node[0]}, y: {node[1]}')
        if node[0] == target_x and node[1] == target_y:
            return cnt

        for move in knights:
            temp_x = node[0] + move[0]
            temp_y = node[1] + move[1]

            if 0 <= temp_x < l and 0 <= temp_y < l and not MAP[temp_x][temp_y]:
                queue.append([temp_x, temp_y])
                MAP[temp_x][temp_y] = True
                ret.append(cnt+1)



# Initial
for _ in range(int(input())):
    l = int(input())
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    print(solution(l, start_x, start_y, target_x, target_y))