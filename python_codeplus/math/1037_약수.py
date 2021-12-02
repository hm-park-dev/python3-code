# 1037 약수
# 29200 KB 68 ms

if __name__ == "__main__":
    
    n = int(input())
    m = list(map(int, input().split()))
    m.sort()

    print(m[0] * m[-1])
