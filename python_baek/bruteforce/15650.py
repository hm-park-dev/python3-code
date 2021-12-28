# 15650.py N과 M (2)
from collections import deque
import itertools

N, M = map(int, input().split())

def solution(visited):
    if len(visited) == M+1:
        # 제일 첫번째 원소 0을 제외한 나머지 출력
        print(' '.join(map(str, list(itertools.islice(visited, 1, M+1)))))
        return
    
    for i in range(1, N+1):
        # 고른 수열은 오름차순이어야 한다.
        if i in visited or i < visited[-1]:
            continue
        visited.append(i)
        solution(visited)
        visited.pop()
    

visited = deque()
visited.append(0)
solution(visited)