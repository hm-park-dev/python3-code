# 11729.py 하노이 탑 이동 순서

def hanoi(start:int, target:int, n:int):
    if n == 1:
        return print(start, target)
    # 목표 지점에 한 개를 옮기기 위해서는 다른 쪽으로 나머지 갯수를 다 보내야함
    hanoi(start, 6-start-target, n-1)
    print(start, target)
    hanoi(6-start-target, target, n-1)

n = int(input())
print(2**n - 1)
hanoi(1, 3, n)