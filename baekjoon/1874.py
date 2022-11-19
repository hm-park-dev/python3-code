# 1874.py 스택 수열

# 1 -> 메모리제한 걸림?: 처음 방식은 ind를 계속 무한히 증가 -> 여기서 걸린듯

from sys import stdin

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]
ans = list()
st = list()
nums = list(range(1, n+1))

for i in range(n):
    while True: 
        if st and st[-1] > arr[i]:
            print('NO')
            exit()
        if not st or st[-1] != arr[i]:
            st.append(nums.pop(0))
            ans.append('+')
        if st and st[-1] == arr[i]:
            st.pop()
            ans.append('-')
            break

for a in ans:
    print(a)