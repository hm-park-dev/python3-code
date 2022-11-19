# 2644.py 촌수계산

N = int(input())
A, B = map(int, input().split())
parents = [0 for _ in range(N+1)]

# 부모의 배열을 만듦
for _ in range(int(input())):
    x, y = map(int, input().split())
    parents[y] = x

A_anc, B_anc = [], []
A_d, B_d = 0, 0

# A의 조상 및 거리
while A > 0:
    A_anc.append((A, A_d))
    A_d += 1
    A = parents[A]

# B의 조상 및 거리
while B > 0:
    B_anc.append((B, B_d))
    B_d += 1
    B = parents[B]

# 같은 조상이 있을 경우 거리의 합 = 촌 수 
for i in A_anc:
    for j in B_anc:
        if i[0] == j[0]:
            print(i[1] + j[1])
            exit()

print(-1)