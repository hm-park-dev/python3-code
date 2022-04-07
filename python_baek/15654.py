# 15654.py N과 M (5)

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = list()

def solution(visited):
    if len(visited) == M:
        print(' '.join(map(str, visited)))
    
    for i in range(N):
        if num[i] in visited:
            continue
        visited.append(num[i])
        solution(visited)
        visited.pop()

solution(visited)