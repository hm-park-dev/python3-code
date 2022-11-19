# 15655 N과 M (6)

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def solution(visited):
    if len(visited) == M+1:
        print(' '.join(map(str, visited[1:])))
        return
    
    for i in range(N):
        # 중복x 오름차순
        if arr[i] in visited or arr[i] < visited[-1]:
            continue
        visited.append(arr[i])
        solution(visited)
        visited.pop()

visited = list()
visited.append(0)
solution(visited)