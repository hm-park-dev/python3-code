# 1406.py 에디터

# 2개의 스택을 사용
pre_str = list(input())
post_str = list()

for _ in range(int(input())):
    command = input()
    # 커서를 왼쪽으로 한 칸 옮김
    if command[0] == 'L':
        if pre_str:
            post_str.append(pre_str.pop())
        else: continue
    elif command[0] == 'D':
        if post_str:
            pre_str.append(post_str.pop())
        else: continue
    elif command[0] == 'B':
        if pre_str:
            pre_str.pop()
        else: continue
    elif command[0] == 'P':
        pre_str.append(command[2])

print(''.join(pre_str + list(reversed(post_str))))