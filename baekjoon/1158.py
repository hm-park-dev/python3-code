# 1158.py 요세푸스 문제
from collections import deque

N, K = map(int, input().split())
dq = deque(range(1, N+1))
ret = list()

while len(dq):
    # deque를 num만큼 회전
    dq.rotate(-(K-1))
    ret.append(dq.popleft())

print(f"<{str(ret)[1:-1]}>")