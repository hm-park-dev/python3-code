# 6588.py 골드바흐의 추축

def era(N: int):
    ck, p = [True for _ in range(N+1)], []
    for i in range(2, N+1):
        if ck[i] == False:
            continue
        p.append(i)
        for j in range(i*2, N+1, i):
            ck[j] = False
    return ck

N = 1000000
ck = era(N)
cl = len(ck)

while True:
    num = int(input())
    if num == 0: break
    flag = 0

    for i in range(3, cl+1):
        if ck[i] and ck[num-i]:
            print(f"{num} = {i} + {num-i}")
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")