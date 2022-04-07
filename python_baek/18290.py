# 18290.py NM과 K (1)

N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
ans = -40000
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 심각한 시간복잡도 visited = list()
# def solution(visited):
#     if len(visited) == K:
#         ret = 0
#         for i in visited:
#             x = i[0]
#             y = i[1]
#             ret += MAP[x][y]

#         global ans
#         ans = max(ans, ret)
#         return
    
#     for i in range(N):
#         for j in range(M):
#             if [i, j] in visited:
#                 continue
#             if len(visited) == 0:
#                 visited.append([i, j])
#                 solution(visited)
#                 visited.pop()
#             else:
#                 for arr in visited:
#                     a, b = arr[0], arr[1]
#                     if a-1 == i and b == j:
#                         break
#                     elif a+1 == i and b == j:
#                         break
#                     elif a == i and b-1 == j:
#                         break
#                     elif a == i and b+1 == j:
#                         break
#                 else:
#                     visited.append([i, j])
#                     solution(visited)
#                     visited.pop()
def solution(px, py, ind, ret):
    if ind == K:
        global ans
        ans = max(ans, ret)
        return
    
    # 아래와 오른쪽로만 이동가능
    for x in range(px, N):
        for y in range(py if x==px else 0, M):
            if visited[x][y]:
                continue

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N  and 0 <= ny < M:
                    if visited[nx][ny]:
                        break
            else:
                visited[x][y] = True
                solution(x, y, ind + 1, ret + MAP[x][y])
                visited[x][y] = False


solution(0, 0, 0, 0)
print(ans)