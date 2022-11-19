# 9095.py 1, 2, 3 더하기

T = int(input())
arr = [0 for _ in range(12)]

arr[1] = 1
arr[2] = 2
arr[3] = 4

# dynamic programming
for i in range(4, 12):
    arr[i] = arr[i-3] + arr[i-2] + arr[i-1]

for _ in range(T):
    n = int(input())
    print(arr[n])