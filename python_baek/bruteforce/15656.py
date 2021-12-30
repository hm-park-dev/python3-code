# 15656.py N과 M (7)

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def solution(visited):
    if len(visited) == M:
        print(' '.join(map(str, visited)))
        return

    for i in range(N):
        visited.append(arr[i])
        solution(visited)
        visited.pop()

visited = list()
solution(visited)