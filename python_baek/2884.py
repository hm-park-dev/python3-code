# 2884.py ěë ěęł

H, M = map(int, input().split())

if M >= 45:
    print(f"{H} {M-45}")
else:
    if H >= 1:
        print(f"{H-1} {60 + M - 45}")
    else:
        print(f"{23} {60 + M - 45}")