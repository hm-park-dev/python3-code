# 2562.py 최댓값

ret = 0
ind = 0
for i in range(9):
    num = int(input())
    if ret < num:
        ret = num
        ind = i + 1
print(ret)
print(ind)