# 1676.py 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

def get_factorial(N: int) -> int:
    if N == 0:
        return 1
    else:
        return N * get_factorial(N-1)

N = int(input())
ret = 0
fact = list(reversed(list(str(get_factorial(N)))))

for i in range(0, len(fact)):
    if fact[i] == '0':
        ret = ret + 1
    else:
        break

print(ret)