# 17087.py 숨바꼭질 6
# https://www.acmicpc.net/problem/17087

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N, S = map(int, input().split())
brothers = list(map(int, input().split()))
ans = 0

if N == 1:
    ans = abs(brothers[0] - S)
else:
    temp = abs(brothers.pop() - S)
    while brothers:
        brother = brothers.pop()
        distance = abs(S - brother)
        if temp >= brother:
            temp = gcd(temp, distance)
        else:
            temp = gcd(distance, temp)
    ans = temp
print(ans)