# 15652.py N과 M (4)

N, M = map(int, input().split())
visited = list()

def solution(visited):
    if len(visited) == M+1:
        # 제일 첫번째 원소 0을 제외한 나머지 출력
        print(' '.join(map(str, visited[1:])))
        return
    
    for i in range(1, N+1):
        # 고른 수열은 비내림차순이어야 한다.
        if i < visited[-1]:
            continue
        visited.append(i)
        solution(visited)
        visited.pop()

visited.append(0)
solution(visited)