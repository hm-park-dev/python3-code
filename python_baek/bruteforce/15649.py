# 15649.py N과 M (1)

N, M = map(int, input().split())

def solution(visited):
    if len(visited) == M:
        print(' '.join(map(str, visited)))
        return
    
    for i in range(1, N+1):
        if i in visited:
            continue
        visited.append(i)
        solution(visited)
        visited.pop()

visited = list()
solution(visited)