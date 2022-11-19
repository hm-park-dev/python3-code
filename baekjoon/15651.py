# 15651.py N과 M (3)

N, M = map(int, input().split())
visited = list()

def solution(visited):

    if len(visited) == M:
        print(' '.join(map(str, visited)))
        return

    # 중복가능
    for i in range(1, N+1):
        visited.append(i)
        solution(visited)
        visited.pop()

solution(visited)