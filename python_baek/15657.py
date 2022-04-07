# 15657.py N과 M (8)

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def solution(visited):
    if len(visited) == M+1:
        # 제일 첫번째 원소 0을 제외한 나머지 출력
        print(' '.join(map(str, visited[1:])))
        return
    
    for i in range(N):
        # 고른 수열은 비내림차순이어야 한다.
        if arr[i] < visited[-1]:
            continue
        visited.append(arr[i])
        solution(visited)
        visited.pop()

visited = list()
visited.append(0)
solution(visited)