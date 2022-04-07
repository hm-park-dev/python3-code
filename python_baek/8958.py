# 8958.py OX퀴즈

def solution(res: list) -> int:
    ret = 0
    point = 0

    for i in range(len(res)):
        if res[i] == 'O':
            ret += 1
            point += ret
        else:
            ret = 0
    return point

for _ in range(int(input())):
    res = list(input())
    print(solution(res))