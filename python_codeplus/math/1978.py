# 1978.py 소수 찾기
import sys
import math

def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    cnt = 0

    for i in range(0, n):
        if num[i] == 1:
            continue
        elif (num[i] == 2) or (num[i] == 5):
            cnt += 1
            print(num[i])
        else:
            if is_prime(num[i]):
                cnt += 1
                print(num[i])

    print(cnt)