# 4673.py 셀프 넘버

def d(n:int) -> int:
    ret = n
    arr = list(str(n))
    for i in arr:
        ret += int(i)
    
    return ret

numbers = set(range(1, 10001))
non_number = set()

for i in range(1, 10001):
    non_number.add(d(i))

self_number = sorted(numbers - non_number)
for i in self_number:
    print(i)