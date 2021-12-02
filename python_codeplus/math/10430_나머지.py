# 10430_나머지.py
# 29200 KB
# 68 ms

import time


if __name__ == '__main__':
    a, b, c = map(int, (input().split()))
    #start = time.time()

    d = a%c
    e = b%c

    print((a+b)%c)
    print((d + e)%c)
    print((a*b)%c)
    print(((d)*(e)%c))
    #print("time: ",  time.time() - start)