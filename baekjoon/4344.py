# 4344.py 평균은 넘겠지

for _ in range(int(input())):
    N, *arr = map(int, input().split())
    avr = sum(arr) / N
    gst = 0
    for i in range(N):
        if arr[i] > avr:
            gst += 1
    print(f"{gst/N * 100:.3f}%")
