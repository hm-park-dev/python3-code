# 1065.py 한수

N = int(input())

def solution(num: int) -> bool:
    arr = list(map(int, list(str(num))))
    l = len(arr)

    if l == 1:
        return True

    de = arr[0] - arr[1]
    for i in range(1, l - 1):
        if de != arr[i] - arr[i+1]:
            break
    else: return True

    return False  


ret = 0
for i in range(1, N+1):
    if solution(i):
        ret += 1
print(ret)