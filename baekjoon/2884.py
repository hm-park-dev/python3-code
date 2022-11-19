# 2884.py 알람 시계

H, M = map(int, input().split())

if M >= 45:
    print(f"{H} {M-45}")
else:
    if H >= 1:
        print(f"{H-1} {60 + M - 45}")
    else:
        print(f"{23} {60 + M - 45}")