# 1107.py 리모컨

N = int(input())
M = int(input())

# 고장난 버튼
if M:
    button = set(input().split())
else:
    button = set()

# 현재 채널
current = 100
# 오직 +/-만 사용했을 때
ret = abs(current - N)
ans = 0

# 이동하려고 하는 채널은 500,000보다 작지만 -하는 경우도 있음
for channel in range(1000001):
    for i in str(channel):
        if i in button:
            break
    # 번호를 눌러서 완성할 수 있음
    # for else: 위의 for문에서 break가 발생하지 않았을 경우에만 돌아감
    else:
        ret = min(ret, abs(channel - N) + len(str(channel)))

print(ret)