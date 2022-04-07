# 2609.py 최대공약수와 최소공배수
import sys

def get_gcd(n: int, m: int) -> int:
    if n < m:
        get_gcd(m, n)
    if m == 0:
        return n
    else:
        return get_gcd(m, n%m)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    gcd = get_gcd(n,m)
    lcm = int(n * m / gcd)

    print(gcd)
    print(lcm)