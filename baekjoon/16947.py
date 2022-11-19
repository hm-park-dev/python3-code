# 16947.py 서울 지하철 2호선
# https://www.acmicpc.net/problem/16947

# n번 역과 순환선 사이의 거리를 출력
# 사이클을 찾아야함?
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(target, cnt, start):
    global cycle_find

    # 다시 방문
    if visited[target]:
        # a -> b -> a is not cycle
        # a -> b -> c -> a is cycle
        # 다시 방문 했으나 그때 거리가 3이상일시
        if cnt >= 3 and target == start:
            # this is cycle start node!
            cycle_find = True
            return target
        # this case, a -> b -> a!
        # or... only visited node
        else:
            return -1

    # target에 방문
    visited[target] = True

    for node in graph[target]:
        # 방문하지 않았다면
        cycle_start_node = dfs(node, cnt + 1, start)

        if cycle_start_node != -1:
            cycle[target] = True
            # 사이클 백트래킹 끝
            # 시작지점까지 되돌아옴
            if target == cycle_start_node:
                return -1
            else:
                return cycle_start_node
    return -1



# Initial
N = int(input())
graph = [[] for _ in range(N + 1)] # 1 ~ N node
cycle = [False for _ in range(N+1)]
visited = [False for _ in range(N+1)]
answer = [0 for _ in range(N+1)] # distance answer
cycle_find = False

for _ in range(N):
    a, b = map(int, input().split())
    # Undirected Graph
    graph[a].append(b)
    graph[b].append(a)


# 1. Find the Cycle Using DFS
for i in range(1, N+1):
    cycle = [False for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    dfs(i, 0, i)
    if cycle_find:
        break
# print('[DEBUG] cycle:', cycle)

# 2. Get the minimum distance Using BFS
queue = deque()

for i in range(1, N+1):
    if cycle[i]:
        # If node is in cycle, distance = 0
        # BFS를 이용해 거리를 구할것이므로
        # 사이클에 속하는 노드부터 뻗어나감
        queue.append(i)
        answer[i] = 0
    else:
        answer[i] = -1

while queue:
    v = queue.popleft()
    for node in graph[v]:
        # node is not in CYCLE
        # 첫 갱신
        if answer[node] == -1:
            queue.append(node)
            # 뻗어나가면서 거리가 1씩 늘어남
            answer[node] = answer[v] + 1

# Answer
print(' '.join(map(str, answer[1:])))