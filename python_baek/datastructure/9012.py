# 9012.py 괄호
# stack

def solution(lst: list) -> bool:
    ret = []

    for i in range(len(lst)):
        if lst[i] == '(':
            ret.append(lst[i])
        else:
            if len(ret) == 0:
                return False
            ret.pop()

    return len(ret) == 0

t = int(input())

for _ in range(t):
    lst = list(input())
    ret = solution(lst)

    if ret == True:
        print("YES")
    else:
        print("NO")