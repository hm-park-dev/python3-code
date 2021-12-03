# 17425_약수의_합.py
import sys

if __name__ == '__main__':
    n_max = 1000000

    f = [1] * (n_max+1)
    g = [0] * (n_max+1)

    # 배수의 원리를 이용해 약수의 합구하기
    for i in range(2, n_max+1):
        j = 1
        while(i*j <= n_max):
            f[i*j] += i
            j += 1
    
    for i in range(1, n_max+1):
        g[i] = g[i-1] + f[i]

    t = int(sys.stdin.readline())
    ans = []
    for n in range(t):
        n = int(sys.stdin.readline())
        ans.append(g[n])

    print('\n'.join(map(str, ans))+'\n')