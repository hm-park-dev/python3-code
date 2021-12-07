# 1929.py 소수 구하기

# 에라토스테네스의 체
def era(N:int):
    ck, p = [False for _ in range(N+1)], []
    for i in range(2, N+1):
        if ck[i] == True:
            continue
        p.append(i)
        for j in range(i*2, N+1, i):
            ck[j] = True
    return p

N = 1000000
prime_num = era(N)
a, b = map(int, input().split())

for i in range(len(prime_num)):
    if prime_num[i] >= a and prime_num[i] <= b:
        print(prime_num[i])